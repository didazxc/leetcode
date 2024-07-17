"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出: [ [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1] ]
"""


def backtracking(nums, path, used, res):
    if len(path) == len(nums):
        res.append(path[:])
        return
    for i in range(len(nums)):
        if used[i]:
            continue
        used[i] = True
        path.append(nums[i])
        backtracking(nums, path, used, res)
        path.pop()
        used[i] = False


def permute(nums):
    res = []
    backtracking(nums, [], [False]*len(nums), res)
    return res


if __name__ == '__main__':
    print(permute([1,2,3]))
