"""Принимаем значения для графа"""
print("Введите количетв вершин и количество ребер")
N, M = map(int, input().split())


graph = {i:set() for i in range(N)}
print("Введите связи в графе")
for i in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)


#Реализуем обход в ширину с помощью очереди

from collections import deque
distances = [None] * N
start_vertex = 0
distances[start_vertex] = 0
queue = deque([start_vertex])

while queue: # пока очеред не пуста
    cur_v = queue.popleft() # достаем первый элемент
    for neigh_v in graph[cur_v]: #проходим всех его соседей
        if distances[neigh_v] is None: # если его ещё не посетили
            distances[neigh_v] = distances[cur_v] + 1
            queue.append(neigh_v) #Добавляем в очередь, чтобы и его соседей проверить

print(graph)
print(distances)
