"""
97. 小明逛公园
题目描述
小明喜欢去公园散步，公园内布置了许多的景点，相互之间通过小路连接，小明希望在观看景点的同时，能够节省体力，走最短的路径。


给定一个公园景点图，图中有 N 个景点（编号为 1 到 N），以及 M 条双向道路连接着这些景点。每条道路上行走的距离都是已知的。


小明有 Q 个观景计划，每个计划都有一个起点 start 和一个终点 end，表示他想从景点 start 前往景点 end。由于小明希望节省体力，他想知道每个观景计划中从起点到终点的最短路径长度。 请你帮助小明计算出每个观景计划的最短路径长度。

输入描述
第一行包含两个整数 N, M, 分别表示景点的数量和道路的数量。

接下来的 M 行，每行包含三个整数 u, v, w，表示景点 u 和景点 v 之间有一条长度为 w 的双向道路。

接下里的一行包含一个整数 Q，表示观景计划的数量。

接下来的 Q 行，每行包含两个整数 start, end，表示一个观景计划的起点和终点。

输出描述
对于每个观景计划，输出一行表示从起点到终点的最短路径长度。如果两个景点之间不存在路径，则输出 -1。
输入示例
7 3
2 3 4
3 6 6
4 7 8
2
2 3
3 4
输出示例
4
-1
提示信息
从 2 到 3 的路径长度为 4，3 到 4 之间并没有道路。

1 <= N, M, Q <= 1000.
"""


def floyd(n, edges, dst):
    """
    grid[i][j]表示i到j最短路径，其实并不合适。因为`grid[i][j] = grid[i][k] + grid[k][j]`需要`grid[i][k]`和`grid[k][j]`已经是最优的。
    因此，我们得构造出一种层次，类似动态规划，使用规模划分层次：grid[i][j][k]表示i到j经过前k个节点的最短路径。
    """
    grid = [[[10005] * (n+1) for _ in range(n+1)] for _ in range(n+1)]
    for i, j, v in edges:
        grid[i][j][0] = v
        grid[j][i][0] = v
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                grid[i][j][k] = min(grid[i][j][k-1], grid[i][k][k-1]+grid[k][j][k-1])
    for start, end in dst:
        if grid[start][end][n] == 10005:
            print(-1)
        else:
            print(grid[start][end][n])


def floyd2(n, edges, dst):
    """
    grid[i][j]表示i到j最短路径，其实并不合适。因为`grid[i][j] = grid[i][k] + grid[k][j]`需要`grid[i][k]`和`grid[k][j]`已经是最优的。
    """
    grid = [[10005] * (n+1) for _ in range(n+1)]
    for i, j, v in edges:
        grid[i][j] = v
        grid[j][i] = v
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                grid[i][j] = min(grid[i][j], grid[i][k]+grid[k][j])
    for start, end in dst:
        if grid[start][end] == 10005:
            print(-1)
        else:
            print(grid[start][end])


if __name__ == '__main__':
    inputs = """
7 3
2 3 4
3 6 6
4 7 8
2
2 3
3 4
    """
    arr = [list(map(int, line.strip().split())) for line in inputs.strip().split('\n')]
    n, m = arr[0]
    edges = arr[1:m+1]
    mm = arr[m+1][0]
    floyd2(n, edges, arr[-mm:])

