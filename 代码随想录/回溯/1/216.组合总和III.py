"""
找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。
示例 1: 输入: k = 3, n = 7 输出: [[1,2,4]]

示例 2: 输入: k = 3, n = 9 输出: [[1,2,6], [1,3,5], [2,3,4]]
"""


def combine_sum(n, k, start, path, res):
    if len(path) == k:
        if sum(path) == n:
            res.append(path[:])
        return
    for i in range(start, 10 - (k - len(path)) + 1):
        path.append(i)
        combine_sum(n, k, i + 1, path, res)
        path.pop()


def combine(n, k):
    path = []
    res = []
    combine_sum(n, k, 1, path, res)
    return res


if __name__ == '__main__':
    print(combine(9, 3))
