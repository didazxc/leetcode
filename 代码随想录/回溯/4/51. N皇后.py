"""
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。

每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
"""


def backtracking(n, path, res):
    nums = len(path)
    if nums == n:
        res.append(path[:])
        return
    for i in range(n):
        seen = []
        for j in range(nums):
            seen.append(path[j])
            seen.append(path[j]+nums-j)
            seen.append(path[j]-nums+j)
        if i in seen:
            continue
        path.append(i)
        backtracking(n, path, res)
        path.pop()


def queue(n):
    res = []
    backtracking(n, [], res)
    result = [[f'{"."*i}Q{"."*(n-1-i)}' for i in arr] for arr in res]
    return result


if __name__ == '__main__':
    print(queue(4))
