"""
【题目描述】

小明是一位科学家，他需要参加一场重要的国际科学大会，以展示自己的最新研究成果。

小明的起点是第一个车站，终点是最后一个车站。然而，途中的各个车站之间的道路状况、交通拥堵程度以及可能的自然因素（如天气变化）等不同，这些因素都会影响每条路径的通行时间。

小明希望能选择一条花费时间最少的路线，以确保他能够尽快到达目的地。

【输入描述】

第一行包含两个正整数，第一个正整数 N 表示一共有 N 个公共汽车站，第二个正整数 M 表示有 M 条公路。

接下来为 M 行，每行包括三个整数，S、E 和 V，代表了从 S 车站可以单向直达 E 车站，并且需要花费 V 单位的时间。

【输出描述】

输出一个整数，代表小明从起点到终点所花费的最小时间。

输入示例

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
输出示例：12

【提示信息】

能够到达的情况：

如下图所示，起始车站为 1 号车站，终点车站为 7 号车站，绿色路线为最短的路线，路线总长度为 12，则输出 12。



不能到达的情况：

如下图所示，当从起始车站不能到达终点车站时，则输出 -1。



数据范围：

1 <= N <= 500; 1 <= M <= 5000;
"""


def dijkstra(n, graph):
    """
    不支持负数权重，而prim用于构建最小生成树可以支持负数权重
    dijkstra在构建路径，固定好后无法回溯，因此负数边无法替换原来路径
    """
    min_dist = [float('inf')] * (n+1)
    visited = [False] * (n+1)
    min_dist[1] = 0
    parent = [0] * (n+1)
    for _ in range(n):
        cur = -1
        cur_min_dist = float('inf')
        for i in range(1, n+1):
            if not visited[i] and min_dist[i] < cur_min_dist:
                cur = i
                cur_min_dist = min_dist[i]
        if cur == -1:
            return -1
        visited[cur] = True
        for j in range(1, n+1):
            dist_j = min_dist[cur] + graph[cur][j]
            if dist_j < min_dist[j]:
                min_dist[j] = dist_j
                parent[j] = cur
    return min_dist[n], parent


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
    arr = [list(map(int, line.strip().split())) for line in inputs.strip().split('\n')]
    v, e = arr[0]
    graph = [[10001]*(v+1) for _ in range(v+1)]
    for i, j, k in arr[1:]:
        graph[i][j] = k
        graph[j][i] = k
    min_dist, parent = dijkstra(v, graph)
    print(min_dist)
    for i in range(1, v+1):
        print(parent[i], '->', i)
