"""
题目描述：

给定一个由 1（陆地）和 0（水）组成的矩阵，你需要计算岛屿的数量。岛屿由水平方向或垂直方向上相邻的陆地连接而成，并且四周都是水域。你可以假设矩阵外均被水包围。

输入描述：

第一行包含两个整数 N, M，表示矩阵的行数和列数。

后续 N 行，每行包含 M 个数字，数字为 1 或者 0。

输出描述：

输出一个整数，表示岛屿的数量。如果不存在岛屿，则输出 0。

输入示例：

4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
输出示例：

3

提示信息



根据测试案例中所展示，岛屿数量共有 3 个，所以输出 3。

数据范围：

1 <= N, M <= 50
"""


def dfs(n, m, graph, i, j, seen):
    directs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    if 0<=i < n and 0<=j < m and not seen[i][j] and graph[i][j] == '1':
        seen[i][j] = True
        for di, dj in directs:
            dfs(n, m, graph, i+di, j+dj, seen)


def islands(n, m, input):
    res = 0
    graph = [line.strip().split() for line in inputs.strip().split('\n')]
    seen = [[False]*m for _ in range(m)]
    for i in range(n):
        for j in range(m):
            if graph[i][j]=='1' and not seen[i][j]:
                res += 1
                bfs(n,m,graph,i,j,seen)
    return res


def bfs(n, m, graph, i, j, seen):
    directs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    seen[i][j] = True
    stack = [(i, j)]
    while stack:
        i,j = stack.pop()
        for di, dj in directs:
            if 0<=i+di < n and 0<=j+dj < m and not seen[i+di][j+dj] and graph[i+di][j+dj] == '1':
                seen[i+di][j+dj] = True
                stack.append((i+di, j+dj))



if __name__ == '__main__':
    n, m = 4, 5
    inputs = """
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1
    """
    print(islands(n, m, inputs))
