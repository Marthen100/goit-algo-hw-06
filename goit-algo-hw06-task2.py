import networkx as nx

# Reusing the previously created graph for the city transportation network
G = nx.Graph()
nodes = ['Station A', 'Station B', 'Station C', 'Station D', 'Station E']
edges = [('Station A', 'Station B'), ('Station B', 'Station C'), ('Station C', 'Station D'),
         ('Station D', 'Station E'), ('Station A', 'Station C'), ('Station B', 'Station D')]
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Function to perform BFS and DFS on the graph
def search_graph(graph, start_node, goal_node, method='bfs'):
    if method == 'bfs':
        # Breadth-first search
        path_generator = nx.bfs_tree(graph, source=start_node)
    else:
        # Depth-first search
        path_generator = nx.dfs_tree(graph, source=start_node)
    
    try:
        # Try to find a path from start_node to goal_node
        path = nx.shortest_path(path_generator, source=start_node, target=goal_node)
    except nx.NetworkXNoPath:
        path = None
        
    return path

# Perform BFS and DFS from 'Station A' to 'Station E'
bfs_path = search_graph(G, 'Station A', 'Station E', method='bfs')
dfs_path = search_graph(G, 'Station A', 'Station E', method='dfs')

bfs_path, dfs_path

print("Breadth-First Search (BFS) Path from 'Station A' to 'Station E':")
print(bfs_path)
print("\nDepth-First Search (DFS) Path from 'Station A' to 'Station E':")
print(dfs_path)