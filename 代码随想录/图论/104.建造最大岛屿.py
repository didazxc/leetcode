"""
题目描述：

给定一个由 1（陆地）和 0（水）组成的矩阵，你最多可以将矩阵中的一格水变为一块陆地，在执行了此操作之后，矩阵中最大的岛屿面积是多少。

岛屿面积的计算方式为组成岛屿的陆地的总数。岛屿是被水包围，并且通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设矩阵外均被水包围。

输入描述：

第一行包含两个整数 N, M，表示矩阵的行数和列数。之后 N 行，每行包含 M 个数字，数字为 1 或者 0，表示岛屿的单元格。

输出描述：

输出一个整数，表示最大的岛屿面积。如果矩阵中不存在岛屿，则输出 0。

输入示例：

4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
输出示例

6

提示信息



对于上面的案例，有两个位置可将 0 变成 1，使得岛屿的面积最大，即 6。



数据范围：

1 <= M, N <= 50。
"""


def dfs(n, m, graph, i, j, mark, cnt):
    directs = [(-1,0),(1,0),(0,-1),(0,1)]
    if 0<=i<n and 0<=j<m and graph[i][j] == 1:
        graph[i][j] = mark
        cnt[mark] = cnt.get(mark, 0) + 1
        for di, dj in directs:
            dfs(n,m,graph,i+di,j+dj,mark,cnt)


def largest_island(n,m,inputs):
    directs = [(-1,0),(1,0),(0,-1),(0,1)]
    graph = [[int(s) for s in line.strip().split()] for line in inputs.strip().split('\n')]
    mark = 2
    cnt = dict()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(n, m, graph, i, j, mark, cnt)
                mark += 1
    res = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                seen = set()
                s = 1
                for di, dj in directs:
                    if 0<=i+di<n and 0<=j+dj<m and graph[i+di][j+dj] > 1:
                        seen.add(graph[i+di][j+dj])
                for mark in seen:
                    s += cnt[mark]
                res = max(res, s)
    return res


if __name__ == '__main__':
    n, m = 4, 5
    inputs = """
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1
    """
    print(largest_island(n,m,inputs))
