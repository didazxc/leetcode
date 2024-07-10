"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。

示例：

输入：s = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
提示：

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
"""
import math


def continue_great(nums, s):
    start = 0
    end = 0
    c = nums[end]
    while c < s and end < len(nums):
        end += 1
        c += nums[end]
    if c < s:
        return 0
    while c - nums[start] >= s:
        c -= nums[start]
        start += 1
    for i in range(end + 1, len(nums)):
        start += 1
        end += 1
        c -= nums[start]
        c += nums[end]
        while c - nums[start] >= s:
            c -= nums[start]
            start += 1
    return end - start + 1


def window(nums, s):
    start = 0
    c = 0
    length = math.inf
    for end in range(len(nums)):
        c += nums[end]
        while c >= s:
            cur_length = end - start + 1
            if cur_length < length:
                length = cur_length
            c -= nums[start]
            start += 1
    return 0 if length == math.inf else length


if __name__ == '__main__':
    print(window([2, 3, 1, 2, 4, 3], 7))
