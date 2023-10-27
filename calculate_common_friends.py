import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import os

# Create the "images" folder if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

# Load the Facebook data for the selected ego node (e.g., "698.edges")
data_file = "facebook_data/facebook/698.edges"
G = nx.read_edgelist(data_file)

# Create a dictionary to store the number of common friends between each pair of friends
common_friends = {}

# Iterate through each edge (friendship)
for u, v in G.edges():
    # Get the neighbors (friends) of nodes u and v
    neighbors_u = set(G[u])
    neighbors_v = set(G[v])
    
    # Calculate the number of common friends between u and v
    num_common_friends = len(neighbors_u.intersection(neighbors_v))
    
    # Store the number of common friends in the dictionary
    common_friends[(u, v)] = num_common_friends

# Calculate the average number of common friends
average_common_friends = np.mean(list(common_friends.values()))

# Print the results
print(f"Average number of common friends: {average_common_friends}")

# Create a histogram of common friends
plt.hist(common_friends.values(), bins=20)
plt.xlabel("Number of Common Friends")
plt.ylabel("Frequency")
plt.title("Distribution of Common Friends")
plt.savefig("images/common_friends_histogram.png")
plt.show()
