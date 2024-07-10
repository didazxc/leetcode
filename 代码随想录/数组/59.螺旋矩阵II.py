"""
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]
"""


def matrix0(n):
    arr = [[0]*n for _ in range(n)]
    row = 0
    k = 1
    while k < n*n:
        for i in range(row, n-row-1):
            arr[row][i] = k
            k += 1
        for i in range(row, n-row-1):
            arr[i][n-row-1] = k
            k += 1
        for j in range(n-row-1, row, -1):
            arr[n-row-1][j] = k
            k += 1
        for j in range(n-row-1, row, -1):
            arr[j][row] = k
            k += 1
        row += 1
    if k == n*n:
        arr[row][row] = k
    return arr


def matrix(n):
    arr = [[0]*n for _ in range(n)]
    k = 1
    direct = 0
    i = 0
    j = 0
    while k <= n*n:
        if arr[i][j] != 0:
            direct += 1
            direct %= 4
        else:
            arr[i][j] = k
            k += 1
        if direct == 0 and j < n-1:
            j += 1
        elif direct == 1 and i < n-1:
            i += 1
        elif direct == 2 and j > 0:
            j -= 1
        elif direct == 3 and i > 0:
            i -= 1
    return arr


if __name__ == '__main__':
    print(matrix(3))




