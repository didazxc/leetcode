"""
题目描述

给定一个由 1（陆地）和 0（水）组成的矩阵，岛屿是被水包围，并且通过水平方向或垂直方向上相邻的陆地连接而成的。

你可以假设矩阵外均被水包围。在矩阵中恰好拥有一个岛屿，假设组成岛屿的陆地边长都为 1，请计算岛屿的周长。岛屿内部没有水域。

输入描述

第一行包含两个整数 N, M，表示矩阵的行数和列数。之后 N 行，每行包含 M 个数字，数字为 1 或者 0，表示岛屿的单元格。

输出描述

输出一个整数，表示岛屿的周长。

输入示例

5 5
0 0 0 0 0
0 1 0 1 0
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0
输出示例

14

提示信息



岛屿的周长为 14。

数据范围：

1 <= M, N <= 50。
"""


def perimeter(graph, n, m):
    cnt = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if graph[i][j]:
                for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if not graph[i+di][j+dj]:
                        cnt += 1
    return cnt


if __name__ == '__main__':
    inputs = """
5 5
0 0 0 0 0
0 1 0 1 0
0 1 1 1 0
0 1 1 1 0
0 0 0 0 0
    """
    arr = [[int(i) for i in line.strip().split()] for line in inputs.strip().split('\n')]
    n, m = arr[0]
    graph = arr[1:]
    print(perimeter(graph, n, m))