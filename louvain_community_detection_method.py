import networkx as nx
from community import community_louvain

# Load the Facebook dataset
data_file = "facebook_data/facebook/698.edges"
G = nx.read_edgelist(data_file)

# Load node attributes from the "698.feat" file
attributes_file = "facebook_data/facebook/698.feat"
attributes = {}
with open(attributes_file, 'r') as file:
    for line in file:
        parts = line.split()
        node_id = int(parts[0])
        attribute_values = list(map(int, parts[1:]))
        attributes[node_id] = attribute_values

# Community Detection
partition = community_louvain.best_partition(G)

# Analyze Homophily
homophily_results = {}
for community_id in set(partition.values()):
    community_nodes = [node for node, comm in partition.items() if comm == community_id]
    community_size = len(community_nodes)
    
    # Initialize counters for attribute matching
    matching_count = 0
    total_possible_matches = 0
    
    for i in range(community_size):
        for j in range(i + 1, community_size):
            node1 = community_nodes[i]
            node2 = community_nodes[j]
            
            # Check if nodes have attributes
            if node1 in attributes and node2 in attributes:
                attribute1 = attributes[node1]
                attribute2 = attributes[node2]
                
                # Calculate the number of matching attributes
                matching_attributes = sum([a1 & a2 for a1, a2 in zip(attribute1, attribute2)])
                matching_count += matching_attributes
                total_possible_matches += len(attribute1)
    
    # Calculate the proportion of attribute matching
    # Check if total_possible_matches is zero
    if total_possible_matches != 0:
        homophily = matching_count / total_possible_matches
    else:
        homophily = 0  # or any other appropriate value

    # Print or use the homophily value
    print("Homophily for Community", community_id, ":", homophily)

    homophily_results[community_id] = homophily

# Print the results
for community_id, homophily in homophily_results.items():
    print(f"Community {community_id}: Homophily = {homophily:.2f}")
