"""
题目描述：

现有一个 N × M 的矩阵，每个单元格包含一个数值，这个数值代表该位置的相对高度。矩阵的左边界和上边界被认为是第一组边界，而矩阵的右边界和下边界被视为第二组边界。

矩阵模拟了一个地形，当雨水落在上面时，水会根据地形的倾斜向低处流动，但只能从较高或等高的地点流向较低或等高并且相邻（上下左右方向）的地点。我们的目标是确定那些单元格，从这些单元格出发的水可以达到第一组边界和第二组边界。

输入描述：

第一行包含两个整数 N 和 M，分别表示矩阵的行数和列数。

后续 N 行，每行包含 M 个整数，表示矩阵中的每个单元格的高度。

输出描述：

输出共有多行，每行输出两个整数，用一个空格隔开，表示可达第一组边界和第二组边界的单元格的坐标，输出顺序任意。

输入示例：

5 5
1 3 1 2 4
1 2 1 3 2
2 4 7 2 1
4 5 6 1 1
1 4 1 2 1
输出示例：

0 4
1 3
2 2
3 0
3 1
3 2
4 0
4 1
提示信息：



图中的蓝色方块上的雨水既能流向第一组边界，也能流向第二组边界。所以最终答案为所有蓝色方块的坐标。

数据范围：

1 <= M, N <= 50
"""


def dfs(n,m,graph,i,j,seen):
    directs = [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]
    for di, dj in directs:
        if 0<=di<n and 0<=dj<m and not seen[di][dj] and graph[di][dj] >= graph[i][j]:
            seen[di][dj] = True
            dfs(n,m,graph,di,dj,seen)


def flow(n,m,inputs):
    graph = [line.strip().split() for line in inputs.strip().split('\n')]
    first_border = [[False]*m for _ in range(n)]
    second_border = [[False]*m for _ in range(n)]
    for i in range(n):
        first_border[i][0] = True
        second_border[i][m-1] = True
        dfs(n,m,graph,i,0,first_border)
        dfs(n,m,graph,i,m-1,second_border)
    for j in range(m):
        first_border[0][j] = True
        second_border[n-1][j] = True
        dfs(n,m,graph,0,j,first_border)
        dfs(n,m,graph,n-1,j,second_border)
    res = []
    for i in range(n):
        for j in range(m):
            if(first_border[i][j] and second_border[i][j]):
                res.append((i, j))
    return res


if __name__ == '__main__':
    n, m = 5, 5
    inputs = """
    1 3 1 2 4
    1 2 1 3 2
    2 4 7 2 1
    4 5 6 1 1
    1 4 1 2 1
    """
    print(flow(n,m,inputs))
