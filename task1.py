import networkx as nx
import matplotlib.pyplot as plt

# Створення порожнього графа
G = nx.Graph()

# Додавання вершин (користувачі)
G.add_nodes_from(["User1", "User2", "User3", "User4", "User5"])

# Додавання зв'язків між вершинами (дружба)
G.add_edges_from([("User1", "User2"), ("User1", "User3"), ("User2", "User3"), ("User4", "User5")])

# Візуалізація графа
nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold', node_size=1500)
plt.title("Соціальна мережа")
plt.show()

# Аналіз основних характеристик
print("Кількість вершин у графі:", G.number_of_nodes())
print("Кількість ребер у графі:", G.number_of_edges())

# Ступінь вершин
print("Ступінь вершин:")
for node in G.nodes():
    print(f"{node}: {G.degree[node]}")