import numpy as np


def find_outgoing_edges(graph, representation, vertex):
    outgoing = []

    if representation == 'adjacency_matrix':
        n = len(graph)
        for j in range(n):
            if graph[vertex][j] == 1:
                outgoing.append((vertex, j))

    elif representation == 'incidence_matrix':
        num_edges = graph.shape[1]
        for col in range(num_edges):
            if graph[vertex][col] == 1:
                for row in range(graph.shape[0]):
                    if graph[row][col] == -1:
                        outgoing.append((vertex, row))
                        break

    elif representation == 'adjacency_list':
        if vertex in graph:
            for neighbor in graph[vertex]:
                outgoing.append((vertex, neighbor))

    elif representation in ['edge_list', 'ordered_edge_list']:
        for u, v in graph:
            if u == vertex:
                outgoing.append((u, v))

    return outgoing


# пример использования
edges = [(0, 3), (0, 4), (1, 0), (2, 0), (2, 3), (2, 4), (2, 1), (3, 1), (3, 4)]
vertices = [0, 1, 2, 3, 4]
n = len(vertices)
m = len(edges)

print(f"Количество вершин: {n}")
print(f"Количество дуг: {m}\n")

# а) Матрица смежности
adj_matrix = np.zeros((n, n), dtype=int)
for u, v in edges:
    adj_matrix[u, v] = 1

print("а) Матрица смежности:")
print(adj_matrix)
print()

# б) Матрица инцидентности
inc_matrix = np.zeros((n, m), dtype=int)
for col_idx, (u, v) in enumerate(edges):
    inc_matrix[u, col_idx] = 1
    inc_matrix[v, col_idx] = -1

print("б) Матрица инцидентности:")
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

# г) Список дуг
print("г) Список дуг:")
print(edges)
print()

# д) Упорядоченный список дуг
ordered_edges = sorted(edges, key=lambda x: (x[0], x[1]))
print("д) Упорядоченный список дуг:")
print(ordered_edges)
print()

print("Задание 3. Дуги, исходящие из вершины:")
for vertex in vertices:
    print(f"\nВершина {vertex}:")
    print(f"  Из списка смежности:      {find_outgoing_edges(adj_list, 'adjacency_list', vertex)}")
    print(f"  Из матрицы смежности:     {find_outgoing_edges(adj_matrix, 'adjacency_matrix', vertex)}")
    print(f"  Из списка дуг:            {find_outgoing_edges(edges, 'edge_list', vertex)}")