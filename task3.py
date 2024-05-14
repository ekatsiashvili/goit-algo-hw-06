import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()
G.add_nodes_from(["User1", "User2", "User3", "User4", "User5"])
G.add_edges_from([("User1", "User2", {'weight': 1}), ("User1", "User3", {'weight': 2}),
                  ("User2", "User3", {'weight': 1}), ("User4", "User5", {'weight': 3})])

# Візуалізація графа
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=1500)
plt.title("Соціальна мережа")
plt.show()

# Алгоритм Дейкстри
shortest_paths = dict(nx.all_pairs_dijkstra_path(G, weight='weight'))
print("Найкоротші шляхи за допомогою алгоритму Дейкстри:")
for source in shortest_paths:
    for target in shortest_paths[source]:
        if source != target:
            path = shortest_paths[source][target]
            distance = nx.shortest_path_length(G, source=source, target=target, weight='weight')
            print(f"{source} -> {target}: {path} (відстань: {distance})")
