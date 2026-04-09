import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


G = nx.Graph()


edges = [(0, 1), (0, 2), (1, 3), (1, 4)]
G.add_edges_from(edges)

def bfs(graph, start):
    visited = []
    queue = dequeue([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(set(graph.neighbours(node))-set(visited))
    return visited

result = bfs(G, 0)
print("BFS Traversal:", result)

nx.draw(G, with_label = True, node_color = 'pink', node_size = 2000)
plt.tittle("Graph for BFS Traversal")
plt.show()
