"""
题目描述

给定一个包含 n 个节点的无向图中，节点编号从 1 到 n （含 1 和 n ）。

你的任务是判断是否有一条从节点 source 出发到节点 destination 的路径存在。

输入描述

第一行包含两个正整数 N 和 M，N 代表节点的个数，M 代表边的个数。

后续 M 行，每行两个正整数 s 和 t，代表从节点 s 与节点 t 之间有一条边。

最后一行包含两个正整数，代表起始节点 source 和目标节点 destination。

输出描述

输出一个整数，代表是否存在从节点 source 到节点 destination 的路径。如果存在，输出 1；否则，输出 0。

输入示例

5 4
1 2
1 3
2 4
3 4
1 4
输出示例

1

提示信息



数据范围：

1 <= M, N <= 100。

"""


class UnionSearch:

    def __init__(self, n):
        self.father = list(range(n+1))

    def find(self, v):
        if v == self.father[v]:
            return v
        else:
            u = self.find(self.father[v])
            self.father[v] = u
            return u

    def is_same(self, u, v):
        u = self.find(u)
        v = self.find(v)
        return u == v

    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.father[v] = u


if __name__ == '__main__':
    inputs = """
5 4
1 2
1 3
2 4
3 4
1 4
    """
    arr = [[int(item) for item in line.strip().split()] for line in inputs.strip().split('\n')]
    n, m = arr[0]
    us = UnionSearch(n)
    for u, v in arr[1:-1]:
        us.join(u, v)
    u, v = arr[-1]
    res = 1 if us.is_same(u, v) else 0
    print(res)
