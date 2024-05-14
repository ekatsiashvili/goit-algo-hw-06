import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()
G.add_nodes_from(["User1", "User2", "User3", "User4", "User5"])
G.add_edges_from([("User1", "User2"), ("User1", "User3"), ("User2", "User3"), ("User4", "User5")])

# Візуалізація графа
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=1500)
plt.title("Соціальна мережа")
plt.show()

# Алгоритм DFS
dfs_paths = list(nx.dfs_edges(G, source="User1"))
print("Шляхи за допомогою DFS:")
for path in dfs_paths:
    print(path)

# Алгоритм BFS
bfs_paths = list(nx.bfs_edges(G, source="User1"))
print("\nШляхи за допомогою BFS:")
for path in bfs_paths:
    print(path)
