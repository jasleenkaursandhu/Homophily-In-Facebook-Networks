import networkx as nx
import matplotlib.pyplot as plt

def custom_facebook_network_analysis(data_file, save_figure=False, output_filename="degree_distribution.png"):
    """
    Custom analysis and visualization of the Facebook network.

    Parameters:
    - data_file: Path to the Facebook network data file (e.g., "facebook_combined.txt").
    - save_figure: Boolean indicating whether to save the histogram plot to an image.
    - output_filename: Filename for the saved image if save_figure is True.

    Returns:
    - G: NetworkX Graph object representing the Facebook network.
    """
    G = nx.Graph()

    # Read the edge data from the file and add it to the graph
    with open(data_file, "r") as f:
        for line in f:
            if line.strip():  # Skip empty lines
                u, v = map(int, line.strip().split())
                G.add_edge(u, v)

    # Calculate and print network properties
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    avg_degree = 2 * num_edges / num_nodes

    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print(f"Average degree: {avg_degree:.2f}")

    # Visualize degree distribution in a histogram
    degrees = [degree for node, degree in G.degree()]
    plt.hist(degrees, bins=30, color='skyblue', edgecolor='black')
    plt.title("Degree Distribution in Facebook Network")
    plt.xlabel("Degree")
    plt.ylabel("Frequency")
    plt.grid(axis='y', alpha=0.75)

    if save_figure:
        plt.savefig(output_filename)

    plt.show()

    return G

# Usage example with saving the visualization to an image
data_file = "facebook_data/facebook_combined.txt"
G = custom_facebook_network_analysis(data_file, save_figure=True, output_filename="degree_distribution.png")
