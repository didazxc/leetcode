from collections import deque


def bellman_ford1(n, edges, src, dst, k):
    min_dist = [float('inf')] * (n+1)
    min_dist[src] = 0
    parent = [0] * (n+1)
    for _ in range(k+1):
        min_dist_cp = min_dist[:]
        for i, j, v in edges:
            if min_dist_cp[i] < float('inf') and min_dist_cp[i] + v < min_dist[j]:
                min_dist[j] = min_dist_cp[i] + v
                parent[j] = i
    return min_dist[dst], parent


def bellman_ford(n, edges, src, dst, k):
    graph = [[] for _ in range(n+1)]
    for i, j, v in edges:
        graph[i].append((j, v))
    min_dist = [float('inf')] * (n+1)
    min_dist[src] = 0
    parent = [0] * (n+1)
    qu = deque()
    qu.append(src)
    while qu and k >= 0:
        k -= 1
        size = len(qu)
        for _ in range(size):
            i = qu.popleft()
            min_dist_copy = min_dist[:]
            for j, k in graph[i]:
                if min_dist_copy[i] < float('inf') and min_dist_copy[i] + k < min_dist_copy[j]:
                    min_dist[j] = min_dist_copy[i] + k
                    parent[j] = i
                    qu.append(j)
    return min_dist[dst], parent


def run(inputs):
    arr = [list(map(int, line.strip().split())) for line in inputs.strip().split('\n')]
    v, e = arr[0]
    src, dst, k = arr[-1]
    min_dist, parent = bellman_ford(v, arr[1:-1], src, dst, k)
    if min_dist is None:
        print('cycle')
    else:
        if min_dist < float('inf'):
            print(min_dist)
        else:
            print('unconnected')
        path = []
        i = v
        while i > 0:
            path.append(i)
            i = parent[i]
        path.reverse()
        print(path)


if __name__ == '__main__':
    inputs = """
6 7
1 2 1
2 4 -3
2 5 2
1 3 5
3 5 1
4 6 4
5 6 -2
2 6 1
    """
    run(inputs)
