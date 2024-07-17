"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出: [ [2], [1], [1,2,2], [2,2], [1,2], [] ]
"""


def combine_track(nums, start_index, path, res):
    res.append(path[:])
    for i in range(start_index, len(nums)):
        if i > start_index and nums[i] == nums[i-1]:
            continue
        path.append(nums[i])
        combine_track(nums, i+1, path, res)
        path.pop()


def combine(nums: list):
    nums.sort()
    res = []
    combine_track(nums, 0, [], res)
    return res


if __name__ == '__main__':
    print(combine([1,2,2]))

