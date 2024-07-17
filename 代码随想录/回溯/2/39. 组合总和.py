"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为： [ [7], [2,2,3] ]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为： [ [2,2,2,2], [2,3,3], [3,5] ]
"""


def combine_sum(nums, target, start, path, res):
    total = sum(path)
    if total == target:
        res.append(path[:])
        return
    if total > target:
        return
    for i in range(start, len(nums)):
        path.append(nums[i])
        combine_sum(nums, target, i, path, res)
        path.pop()


def combine(nums, target):
    res = []
    combine_sum(nums, target, 0, [], res)
    return res


if __name__ == '__main__':
    print(combine([2,3,5], 8))
