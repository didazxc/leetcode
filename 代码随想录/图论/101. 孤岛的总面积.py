"""
题目描述

给定一个由 1（陆地）和 0（水）组成的矩阵，岛屿指的是由水平或垂直方向上相邻的陆地单元格组成的区域，且完全被水域单元格包围。孤岛是那些位于矩阵内部、所有单元格都不接触边缘的岛屿。

现在你需要计算所有孤岛的总面积，岛屿面积的计算方式为组成岛屿的陆地的总数。

输入描述

第一行包含两个整数 N, M，表示矩阵的行数和列数。之后 N 行，每行包含 M 个数字，数字为 1 或者 0。

输出描述

输出一个整数，表示所有孤岛的总面积，如果不存在孤岛，则输出 0。

输入示例

4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
输出示例：

1

提示信息：



在矩阵中心部分的岛屿，因为没有任何一个单元格接触到矩阵边缘，所以该岛屿属于孤岛，总面积为 1。

数据范围：

1 <= M, N <= 50。
"""


def dfs1(n,m,graph,i,j):
    graph[i][j] = '0'
    directs = [(-1,0),(1,0),(0,-1),(0,1)]
    for di, dj in directs:
        if 0<=i+di<n and 0<=j+dj<m and graph[i+di][j+dj] == '1':
            dfs(n,m,graph,i+di,j+dj)


def dfs(n,m,graph,i,j):
    directs = [(-1,0),(1,0),(0,-1),(0,1)]
    if 0<=i<n and 0<=j<m and graph[i][j] == '1':
        graph[i][j] = '0'
        for di, dj in directs:
            dfs(n,m,graph,i+di,j+dj)


def bfs(n,m,graph,i,j):
    directs = [(-1,0),(1,0),(0,-1),(0,1)]
    graph[i][j] = '0'
    stack = [(i,j)]
    while stack:
        i,j = stack.pop()
        for di, dj in directs:
            if 0<=i+di<n and 0<=j+dj<m and graph[i+di][j+dj] == '1':
                graph[i+di][j+dj] = '0'
                stack.append((i+di, j+dj))


def island(n,m,inputs):
    graph = [line.strip().split() for line in inputs.strip().split('\n')]
    res = 0
    for j in range(m):
        if graph[0][j] == '1':
            bfs(n,m,graph,0,j)
        if graph[n-1][j] == '1':
            bfs(n,m,graph,n-1,j)
    for i in range(n):
        if graph[i][0] == '1':
            bfs(n,m,graph,i,0)
        if graph[i][m-1] == '1':
            bfs(n,m,graph,i,m-1)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '1':
                res += 1
    return res


if __name__ == '__main__':
    n, m = 4, 5
    inputs = """
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1
    """
    print(island(n,m,inputs))
