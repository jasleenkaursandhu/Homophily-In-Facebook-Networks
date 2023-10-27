import networkx as nx
import matplotlib.pyplot as plt
import os

# Create the "images" folder if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

# Load the Facebook data for the selected ego node (e.g., "698.edges")
data_file = "facebook_data/facebook/698.edges"
G = nx.read_edgelist(data_file)

# Load the feature data for the selected ego node (e.g., "698.feat")
feat_file = "facebook_data/facebook/698.feat"
with open(feat_file, "r") as f:
    features = f.readline().strip().split(" ")

# Select the attribute to analyze (e.g., "location")
attribute_index = 35  # Adjust this index for the "location" attribute

# Create two lists to store the edges with matching and non-matching attributes
matching_edges = []
non_matching_edges = []

# Iterate through each edge (friendship) and check the attribute
for u, v in G.edges():
    # Check if both u and v are within the range of available features
    if int(u) < len(features) and int(v) < len(features):
        if features[int(u)] == features[int(v)]:
            matching_edges.append((u, v))
        else:
            non_matching_edges.append((u, v))

# Calculate the proportion of matching edges
if len(matching_edges) + len(non_matching_edges) > 0:
    proportion_matching = len(matching_edges) / (len(matching_edges) + len(non_matching_edges))
    print(f"Proportion of matching location attribute edges: {proportion_matching:.2f}")
else:
    print("No edges with attributes found.")

# Create a visualization of the network, differentiating matching and non-matching location attribute edges with colors
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=10, node_color="black")
nx.draw_networkx_edges(G, pos, edgelist=matching_edges, edge_color="green", alpha=0.5)
nx.draw_networkx_edges(G, pos, edgelist=non_matching_edges, edge_color="red", alpha=0.5)
plt.axis("off")
plt.savefig("images/network_with_location.png")
plt.show()
