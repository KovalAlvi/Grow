from collections import deque


def main():
    G = read_graph()
    start = input("С какой верщины начать?")
    while start not in G:
        start = input("С какой верщины начать?")
    shortest_distances = dijkstra(G, start)

    finish = input("До какой вершины считать?")
    while finish not in G:
        finish = input("Нет, такой!!! До какой вершины считать?)

    shortest_path = reveal_shortest_path(G, start, finish, shortest_distances)

def read_graph():
    M = int(input())
    G ={}
    for i in range(M):
        a, b, weight = input().split()
        weight = float(weight)
        add_edge(G, a, b, weight)
        add_edge(G, b, a, weight)
    return G
def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = {b:weight}
    else:
        G[a][b] = weight


def dijkstra(G, start):
    Q = deque()
    s = {}
    s[start] = 0
    Q.append(start)

    while Q:
        v = Q.popleft()
        for u in G[v]:
            if (u not in s) or s[v] + G[v][u] < s[u]:
                s[u] = s[v] + G[v][u]
                Q.append(u)



if __name__ == "__main__":
    main()
