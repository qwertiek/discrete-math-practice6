import numpy as np

edges = [(0, 3), (0, 4), (1, 0), (2, 0), (2, 3), (2, 4), (2, 1), (3, 1), (3, 4)]
vertices = [0, 1, 2, 3, 4]
n = len(vertices)
m = len(edges)

print(f"Количество вершин: {n}")
print(f"Количество дуг: {m}\n")

# а) Матрица смежности (n x n)
adj_matrix = np.zeros((n, n), dtype=int)
for u, v in edges:
    adj_matrix[u, v] = 1

print("а) Матрица смежности:")
print(adj_matrix)
print()

# б) Матрица инцидентности (n x m)
# +1 - дуга исходит из вершины; -1 - дуга входит в вершину; 0  - в ином случае
inc_matrix = np.zeros((n, m), dtype=int)
for col_idx, (u, v) in enumerate(edges):
    inc_matrix[u, col_idx] = 1   # исходит из u
    inc_matrix[v, col_idx] = -1  # входит в v

print("б) Матрица инцидентности (столбцы соответствуют дугам):")
print("Дуги:", edges)
print(inc_matrix)
print()

# в) Список смежности
adj_list = {i: [] for i in range(n)}
for u, v in edges:
    adj_list[u].append(v)

print("в) Список смежности:")
for vertex in sorted(adj_list.keys()):
    print(f"  {vertex} -> {adj_list[vertex]}")
print()

print("г) Список дуг:")
print(edges)
print()

ordered_edges = sorted(edges, key=lambda x: (x[0], x[1]))
print("д) Упорядоченный список дуг:")
print(ordered_edges)