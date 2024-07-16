"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例: 输入: n = 4, k = 2 输出: [ [2,4], [3,4], [2,3], [1,2], [1,3], [1,4], ]
"""


def back_tracking(n, k, start_index, path, res):
    if len(path) == k:
        res.append(path[:])
        return
    for i in range(start_index, n + 1 - (k - len(path)) + 1):
        path.append(i)
        back_tracking(n, k, i + 1, path, res)
        path.pop()


def combine(n, k):
    res = []
    path = []
    back_tracking(n, k, 1, path, res)
    return res


if __name__ == '__main__':
    print(combine(5, 3))
