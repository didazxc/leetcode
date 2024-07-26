"""
卡码网：53. 寻宝

题目描述：

在世界的某个区域，有一些分散的神秘岛屿，每个岛屿上都有一种珍稀的资源或者宝藏。国王打算在这些岛屿上建公路，方便运输。

不同岛屿之间，路途距离不同，国王希望你可以规划建公路的方案，如何可以以最短的总公路距离将 所有岛屿联通起来。

给定一张地图，其中包括了所有的岛屿，以及它们之间的距离。以最小化公路建设长度，确保可以链接到所有岛屿。

输入描述：

第一行包含两个整数V 和 E，V代表顶点数，E代表边数 。顶点编号是从1到V。例如：V=2，一个有两个顶点，分别是1和2。

接下来共有 E 行，每行三个整数 v1，v2 和 val，v1 和 v2 为边的起点和终点，val代表边的权值。

输出描述：

输出联通所有岛屿的最小路径总距离

输入示例：

7 11
1 2 1
1 3 1
1 5 2
2 6 1
2 4 2
2 3 2
3 4 1
4 5 1
5 6 2
5 7 1
6 7 1
输出示例：

6
"""


def prim(n, graph):
    """更新最小距离数组，构建最小生成树"""
    min_dist = [10001]*(n+1)
    in_graph = [False]*(n+1)
    parent = [0]*(n+1)
    for _ in range(1, n):
        cur = -1
        cur_min_dist = float('inf')
        for i in range(1, n+1):
            if not in_graph[i] and min_dist[i] < cur_min_dist:
                cur = i
                cur_min_dist = min_dist[i]
        in_graph[cur] = True
        for i in range(1, n+1):
            if not in_graph[i] and min_dist[i] > graph[cur][i]:
                min_dist[i] = graph[cur][i]
                parent[i] = cur
    return sum(min_dist[2:]), parent


if __name__ == '__main__':
    inputs = """
7 11
1 2 1
1 3 1
1 5 2
2 6 1
2 4 2
2 3 2
3 4 1
4 5 1
5 6 2
5 7 1
6 7 1
    """
    arr = [list(map(int, line.strip().split())) for line in inputs.strip().split('\n')]
    v, e = arr[0]
    graph = [[10001]*(v+1) for _ in range(v+1)]
    for i, j, k in arr[1:]:
        graph[i][j] = k
        graph[j][i] = k
    min_dist, parent = prim(v, graph)
    print(min_dist)
    for i in range(1, v+1):
        print(parent[i], '->', i)

