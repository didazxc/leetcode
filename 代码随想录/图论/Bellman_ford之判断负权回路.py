

def bellman_ford1(n, edges):
    min_dist = [float('inf')] * (n+1)
    min_dist[1] = 0
    parent = [0] * (n+1)
    for _ in range(n-1):
        for i, j, k in edges:
            if min_dist[i] < float('inf') and min_dist[i] + k < min_dist[j]:
                min_dist[j] = min_dist[i] + k
                parent[j] = i
    for i, j, k in edges:
        if min_dist[i] < float('inf') and min_dist[i] + k < min_dist[j]:
            return None, None
    return min_dist[n], parent


def bellman_ford(n, edges):
    graph = [[] for _ in range(n+1)]
    for i, j, k in edges:
        graph[i].append((j, k))
    min_dist = [float('inf')] * (n+1)
    min_dist[1] = 0
    parent = [0] * (n+1)
    count = [0] * (n+1)
    qu = [1]
    while qu:
        i = qu.pop()
        for j, k in graph[i]:
            if min_dist[i] < float('inf') and min_dist[i] + k < min_dist[j]:
                min_dist[j] = min_dist[i] + k
                parent[j] = i
                qu.append(j)
                count[j] += 1
                if count[j] >= n:
                    return None, None
    return min_dist[n], parent


def run(inputs):
    arr = [list(map(int, line.strip().split())) for line in inputs.strip().split('\n')]
    v, e = arr[0]
    min_dist, parent = bellman_ford(v, arr[1:])
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
4 4
1 2 -1
2 3 1
3 1 -1
3 4 1
    """
    run(inputs)
