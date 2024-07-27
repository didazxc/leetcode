import heapq


def dijkstra(n, graph):
    min_dist = [float('inf')] * (n+1)
    min_dist[1] = 0
    visited = [False] * (n+1)
    parent = [0] * (n+1)
    pq = []
    heapq.heappush(pq, (min_dist[1], 1))
    while pq:
        _, i = heapq.heappop(pq)
        visited[i] = True
        for j, v in graph[i]:
            if not visited[j] and min_dist[i] + v < min_dist[j]:
                min_dist[j] = min_dist[i] + v
                parent[j] = i
                heapq.heappush(pq, (min_dist[j], j))
    return min_dist[n], parent


def run(inputs):
    arr = [list(map(int, line.strip().split())) for line in inputs.strip().split('\n')]
    v, e = arr[0]
    graph = [[] for _ in range(v + 1)]
    for i, j, k in arr[1:]:
        graph[i].append((j, k))
    min_dist, parent = dijkstra(v, graph)
    print(min_dist)
    path = []
    i = v
    while i > 0:
        path.append(i)
        i = parent[i]
    path.reverse()
    print(path)


if __name__ == '__main__':
    inputs = """
7 9
1 2 1
1 3 4
2 3 2
2 4 5
3 4 2
4 5 3
2 6 4
5 7 4
6 7 9
    """
    run(inputs)
