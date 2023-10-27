import networkx as nx

# Load the Facebook network graph 
data_file = "facebook_data/facebook_combined.txt"
G = nx.read_edgelist(data_file)

# Calculate degree centrality
degree_centrality = nx.degree_centrality(G)

# Calculate eigenvector centrality
eigenvector_centrality = nx.eigenvector_centrality(G)

# Calculate betweenness centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Print results
for node in G.nodes():
    print(f"Node {node}:")
    print(f"Degree Centrality = {degree_centrality[node]:.4f}")
    print(f"Eigenvector Centrality = {eigenvector_centrality[node]:.4f}")
    print(f"Betweenness Centrality = {betweenness_centrality[node]:.4f}")
    print()
