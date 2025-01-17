"""
给定一个整型数组, 你的任务是找到所有该数组的递增子序列，递增子序列的长度至少是2。

示例:

输入: [4, 6, 7, 7]
输出: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
说明:

给定数组的长度不会超过15。
数组中的整数范围是 [-100,100]。
给定数组中可能包含重复数字，相等的数字应该被视为递增的一种情况。
"""


def track(nums, start_index, path, res):
    if len(path) >= 2:
        res.append(path[:])
    seen = set()
    for i in range(start_index, len(nums)):
        if len(path) == 0 or (nums[i] >= path[-1] and nums[i] not in seen):
            seen.add(nums[i])
            path.append(nums[i])
            track(nums, i+1, path, res)
            path.pop()


def combine(nums):
    res = []
    track(nums, 0, [], res)
    return res


if __name__ == '__main__':
    print(combine([4, 6, 7, 7]))
