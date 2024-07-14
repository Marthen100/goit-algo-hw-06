import networkx as nx
import heapq
import matplotlib.pyplot as plt

# Create a weighted graph to model a city's transportation network
G = nx.Graph()

# Define stations and connections with weights representing distances or travel times
edges_with_weights = [
    ('Station A', 'Station B', 4),
    ('Station B', 'Station C', 3),
    ('Station C', 'Station D', 5),
    ('Station D', 'Station E', 2),
    ('Station A', 'Station C', 8),
    ('Station B', 'Station D', 6)
]
G.add_weighted_edges_from(edges_with_weights)

# Draw the graph
plt.figure(figsize=(8, 5))
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='k', font_size=15, font_weight='bold')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("City Transportation Network Graph")
plt.show()

# Implement DFS and BFS
def bfs(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

def dfs(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Example usage of DFS and BFS
print("DFS Paths:")
for path in dfs(G, 'Station A', 'Station E'):
    print(path)

print("\nBFS Paths:")
for path in bfs(G, 'Station A', 'Station E'):
    print(path)

# Implement Dijkstra's Algorithm using heapq
def dijkstra(graph, start):
    heap = []
    heapq.heappush(heap, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    path = {node: [] for node in graph}
    path[start] = [start]

    while heap:
        (current_distance, current_node) = heapq.heappop(heap)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))
                path[neighbor] = path[current_node] + [neighbor]

    return distances, path

# Finding shortest paths from Station A to all others
distances, paths = dijkstra(G, 'Station A')
print("\nDijkstra's Shortest Paths from Station A:")
for destination in paths:
    print(f"Path to {destination}: {paths[destination]}, Distance: {distances[destination]}")
