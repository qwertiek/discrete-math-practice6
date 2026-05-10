import numpy as np


def convert_graph(graph, from_repr, to_repr):
    # Сначала переведем в единый формат = список дуг
    edges = []

    if from_repr == 'adjacency_matrix':
        n = len(graph)
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 1:
                    edges.append((i, j))

    elif from_repr == 'incidence_matrix':
        n, m = graph.shape
        for col in range(m):
            u, v = -1, -1
            for row in range(n):
                if graph[row][col] == 1:
                    u = row
                elif graph[row][col] == -1:
                    v = row
            if u != -1 and v != -1:
                edges.append((u, v))

    elif from_repr == 'adjacency_list':
        for u in graph:
            for v in graph[u]:
                edges.append((u, v))

    elif from_repr == 'edge_list':
        edges = graph.copy()

    else:
        raise ValueError("Неизвестное представление")

    # Теперь в требуемое представление
    if to_repr == 'edge_list':
        return edges

    elif to_repr == 'adjacency_list':
        vertices = set()
        for u, v in edges:
            vertices.add(u)
            vertices.add(v)
        n = max(vertices) + 1
        adj_list = {i: [] for i in range(n)}
        for u, v in edges:
            adj_list[u].append(v)
        return adj_list

    elif to_repr == 'adjacency_matrix':
        vertices = set()
        for u, v in edges:
            vertices.add(u)
            vertices.add(v)
        n = max(vertices) + 1
        adj_matrix = np.zeros((n, n), dtype=int)
        for u, v in edges:
            adj_matrix[u, v] = 1
        return adj_matrix

    elif to_repr == 'incidence_matrix':
        vertices = set()
        for u, v in edges:
            vertices.add(u)
            vertices.add(v)
        n = max(vertices) + 1
        m = len(edges)
        inc_matrix = np.zeros((n, m), dtype=int)
        for col_idx, (u, v) in enumerate(edges):
            inc_matrix[u, col_idx] = 1
            inc_matrix[v, col_idx] = -1
        return inc_matrix

    else:
        raise ValueError("Неизвестное представление")


# пример
edges = [(0, 3), (0, 4), (1, 0), (2, 0), (2, 3), (2, 4), (2, 1), (3, 1), (3, 4)]
n = 5
m = len(edges)

adj_matrix = np.zeros((n, n), dtype=int)
for u, v in edges:
    adj_matrix[u, v] = 1

inc_matrix = np.zeros((n, m), dtype=int)
for col_idx, (u, v) in enumerate(edges):
    inc_matrix[u, col_idx] = 1
    inc_matrix[v, col_idx] = -1

adj_list = {i: [] for i in range(n)}
for u, v in edges:
    adj_list[u].append(v)

edge_list = edges.copy()

print("Задание 4. Перевод графа из одного представления в другое")

print("\n1. Список дуг -> Матрица смежности")
result = convert_graph(edge_list, 'edge_list', 'adjacency_matrix')
print(result)

print("\n2. Матрица смежности -> Список смежности")
result = convert_graph(adj_matrix, 'adjacency_matrix', 'adjacency_list')
for v in sorted(result.keys()):
    print(f"  {v} -> {result[v]}")

print("\n3. Список смежности -> Матрица инцидентности")
result = convert_graph(adj_list, 'adjacency_list', 'incidence_matrix')
print(result)

print("\n4. Матрица инцидентности -> Список дуг")
result = convert_graph(inc_matrix, 'incidence_matrix', 'edge_list')
print(result)

print("\n5. Матрица смежности -> Список дуг")
result = convert_graph(adj_matrix, 'adjacency_matrix', 'edge_list')
print(result)

print("\n6. Список дуг -> Список смежности")
result = convert_graph(edge_list, 'edge_list', 'adjacency_list')
for v in sorted(result.keys()):
    print(f"  {v} -> {result[v]}")