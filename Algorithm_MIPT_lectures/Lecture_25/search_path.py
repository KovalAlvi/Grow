from collections import deque

graph = { 0:{2,1, 3},
          1: {0, 2},
          2: {3,0,1},
          3: {2,1, 0}}


N = len(graph)
start_vertex = 0
end_vertex = 3
parents = [None] * N
distances = [None] * N

distances[start_vertex] = 0
queue = deque([start_vertex])

for key in graph: # Вывод нашего графа
    print(key, graph[key])

for v in graph[0]: # Доступ до элемента из множества
    print(v)

#Обход в ширину для нахождения самого оптимально пути
while queue:
    u = queue.popleft()
    for v in graph[u]:
        if distances[v] is None:
            distances[v] = distances[u] +1
            parents[v] = u
            queue.append(v)
path = [end_vertex]
parent = parents[end_vertex]

while not parent is None:
    path.append(parent)
    parent = parents[parent]

print("Наиболее оптимальный путь из {} до {}".format(start_vertex, end_vertex), path[::-1])
