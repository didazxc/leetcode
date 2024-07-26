"""
题目描述

给定一个由 1（陆地）和 0（水）组成的矩阵，计算岛屿的最大面积。岛屿面积的计算方式为组成岛屿的陆地的总数。岛屿由水平方向或垂直方向上相邻的陆地连接而成，并且四周都是水域。你可以假设矩阵外均被水包围。

输入描述

第一行包含两个整数 N, M，表示矩阵的行数和列数。后续 N 行，每行包含 M 个数字，数字为 1 或者 0，表示岛屿的单元格。

输出描述

输出一个整数，表示岛屿的最大面积。如果不存在岛屿，则输出 0。

输入示例

4 5
1 1 0 0 0
1 1 0 0 0
0 0 1 0 0
0 0 0 1 1
输出示例

4

提示信息



样例输入中，岛屿的最大面积为 4。

数据范围：

1 <= M, N <= 50。
"""


class Island:

    def __init__(self):
        self.area = 0

    def dfs(self, n, m, graph, i, j, seen):
        directs = [(-1,0),(1,0),(0,-1),(0,1)]
        if 0 <= i < n and 0 <= j < m and not seen[i][j] and graph[i][j] == '1':
            seen[i][j] = True
            self.area += 1
            for di, dj in directs:
                self.dfs(n,m,graph, i+di, j+dj, seen)

    def bfs(self, n,m,graph,i,j,seen):
        self.area = 1
        seen[i][j] = True
        stack = [(i, j)]
        directs = [(-1,0),(1,0),(0,-1),(0,1)]
        while stack:
            i, j = stack.pop()
            for di, dj in directs:
                if 0<=i+di < n and 0<=j+dj < m and not seen[i+di][j+dj] and graph[i+di][j+dj] == '1':
                    seen[i+di][j+dj] = True
                    self.area += 1
                    stack.append((i+di, j+dj))


    def max_area(self, n, m, inputs):
        res = 0
        graph = [line.strip().split() for line in inputs.strip().split('\n')]
        seen = [[False]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if graph[i][j] == '1' and not seen[i][j]:
                    self.area = 0
                    self.bfs(n, m, graph, i, j, seen)
                    res = max(res, self.area)
        return res


if __name__ == '__main__':
    n, m = 4, 5
    inputs = """
    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1
    """
    s = Island().max_area(n, m, inputs)
    print(s)
