import networkx as nx
import matplotlib.pyplot as plt
import os

# Path to the directory containing the ego nodes
ego_data_directory = "facebook_data/facebook/"

# Create an empty graph
G = nx.Graph()

# Iterate through all ego nodes and add edges to the graph
for file in os.listdir(ego_data_directory):
    if file.endswith(".edges"):
        ego_node_id = os.path.splitext(file)[0]
        edges_file = os.path.join(ego_data_directory, file)

        with open(edges_file, "r") as file:
            for line in file:
                u, v = line.strip().split()
                G.add_edge(u, v)

# Use Kamada-Kawai layout
pos = nx.kamada_kawai_layout(G)

# Draw nodes and labels
node_labels = {node: node for node in G.nodes()}
node_size = 10

# Customize node colors if you have attributes to visualize
# node_colors = [your_color_map[attr] for attr in node_attributes]

plt.figure(figsize=(12, 12))
nx.draw(G, pos, with_labels=True, labels=node_labels, node_size=node_size, node_color='lightblue', font_size=6)

plt.title("Facebook Network for All Ego Nodes")
plt.axis("off")
plt.show()
