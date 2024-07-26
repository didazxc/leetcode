"""
题目描述

字典 strList 中从字符串 beginStr 和 endStr 的转换序列是一个按下述规格形成的序列：

序列中第一个字符串是 beginStr。

序列中最后一个字符串是 endStr。

每次转换只能改变一个字符。

转换过程中的中间字符串必须是字典 strList 中的字符串。

给你两个字符串 beginStr 和 endStr 和一个字典 strList，找到从 beginStr 到 endStr 的最短转换序列中的字符串数目。如果不存在这样的转换序列，返回 0。

输入描述

第一行包含一个整数 N，表示字典 strList 中的字符串数量。 第二行包含两个字符串，用空格隔开，分别代表 beginStr 和 endStr。 后续 N 行，每行一个字符串，代表 strList 中的字符串。

输出描述

输出一个整数，代表从 beginStr 转换到 endStr 需要的最短转换序列中的字符串数量。如果不存在这样的转换序列，则输出 0。

输入示例

6
abc def
efc
dbc
ebc
dec
dfc
yhn
输出示例

4

提示信息

从 startStr 到 endStr，在 strList 中最短的路径为 abc -> dbc -> dec -> def，所以输出结果为 4

数据范围：

2 <= N <= 500
"""


def bfs(graph):
    n = len(graph)
    stack = [0]
    res = 1
    seen = set()
    while stack:
        res += 1
        for _ in range(len(stack)):
            i = stack.pop()
            seen.add(i)
            for j in range(n):
                if graph[i][j] and j not in seen:
                    if j == n-1:
                        return res
                    stack.append(j)
    return res


def diff_one(a, b):
    cnt = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            cnt += 1
            if cnt > 1:
                return False
    return cnt == 1


def ladder(n, start, end, strs):
    graph = [[False] * (n+2) for _ in range(n+2)]
    li = [start] + strs + [end]
    for i in range(n+1):
        for j in range(1, n+2):
            graph[i][j] = diff_one(li[i], li[j])
    return bfs(graph)


if __name__ == '__main__':
    inputs = """
6
abc def
efc
dbc
ebc
dec
dfc
yhn
    """
    arr = inputs.strip().split('\n')
    n = int(arr[0])
    start, end = arr[1].split()
    strs = arr[2:]
    print(ladder(n, start, end, strs))

