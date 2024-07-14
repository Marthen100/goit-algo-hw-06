import networkx as nx
import matplotlib.pyplot as plt

# Create a graph instance using NetworkX
G = nx.Graph()

# Adding nodes and edges simulating a simple city's transportation network
# Nodes can represent stations or stops
# Edges represent direct routes between stations

# Adding nodes
nodes = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E']
G.add_nodes_from(nodes)

# Adding edges
edges = [('Station A', 'Station B'), ('Station B', 'Station C'), ('Station C', 'Station D'),
         ('Station D', 'Station E'), ('Station A', 'Station C'), ('Station B', 'Station D')]
G.add_edges_from(edges)

# Drawing the graph
plt.figure(figsize=(8, 5))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=15, font_weight='bold')
plt.title("City Transportation Network Graph")
plt.show()

# Analyzing the graph
num_vertices = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_of_vertices = dict(G.degree())

# Print analysis results
print("Number of vertices:", num_vertices)
print("Number of edges:", num_edges)
print("Degree of vertices:", degree_of_vertices)