"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9

所以返回 [0, 1]
"""


def binary_sum0(nums, target):
    m = dict()
    for i in range(nums):
        num = nums[i]
        if target - num in m:
            return [i, m[target - num]]
        else:
            m[num] = i
    return None


def binary_sum(nums, target):
    arr = sorted(enumerate(nums), key=lambda x: x[1])
    left = 0
    right = len(nums) - 1
    while left < right:
        if arr[left][1] + arr[right][1] == target:
            return [arr[left][0], arr[right][0]]
        elif arr[left][1] + arr[right][1] > target:
            right -= 1
        else:
            left += 1
    return None


