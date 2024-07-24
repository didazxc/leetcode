"""
题目描述：

给定一个由 1（陆地）和 0（水）组成的矩阵，岛屿指的是由水平或垂直方向上相邻的陆地单元格组成的区域，且完全被水域单元格包围。孤岛是那些位于矩阵内部、所有单元格都不接触边缘的岛屿。

现在你需要将所有孤岛“沉没”，即将孤岛中的所有陆地单元格（1）转变为水域单元格（0）。

输入描述：

第一行包含两个整数 N, M，表示矩阵的行数和列数。

之后 N 行，每行包含 M 个数字，数字为 1 或者 0，表示岛屿的单元格。

输出描述

输出将孤岛“沉没”之后的岛屿矩阵。

输入示例：

4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
输出示例：

1 1 0 0 0
1 1 0 0 0
0 0 0 0 0
0 0 0 1 1
提示信息：



将孤岛沉没：



数据范围：

1 <= M, N <= 50
"""


def dfs(n,m,graph,i,j):
    directs = [(-1,0),(1,0),(0,-1),(0,1)]
    if 0<=i<n and 0<=j<m and graph[i][j] == '1':
        graph[i][j] = '2'
        for di, dj in directs:
            dfs(n,m,graph,i+di,j+dj)


def island(n,m,inputs):
    graph = [line.strip().split() for line in inputs.strip().split('\n')]
    for j in range(m):
        dfs(n,m,graph,0,j)
        dfs(n,m,graph,n-1,j)
    for i in range(n):
        dfs(n,m,graph,i,0)
        dfs(n,m,graph,i,m-1)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == '1':
                graph[i][j] = '0'
            elif graph[i][j] == '2':
                graph[i][j] = '1'
    return graph


if __name__ == '__main__':
    n, m = 4, 5
    inputs = """
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1
    """
    print(island(n,m,inputs))