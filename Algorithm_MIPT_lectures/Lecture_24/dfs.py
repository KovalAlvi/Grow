def dfs(vertex, G, used ):
    """Алгоритм обхода в глубину графа
    Не ориентированный графа
    """
    used.add(vertex)
    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour, G, used)

used = set()
N = 0
G = {
    'A' : {'B'},
    'B': {'A', 'C'},
    'C': {'B', 'D'},
    'D': {'C'},
    'E': set()
}
for vertex in G: #Считает компоненты связности. Если можно вс обойти, то 1. Если нет, то два
    if vertex not in used:
        dfs(vertex, G, used)
        N += 1
print(N)
print(used)
