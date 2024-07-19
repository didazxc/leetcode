"""
题目难易：中等

给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意: 每个数组中的元素不会超过 100 数组的大小不会超过 200

示例 1:

输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].
示例 2:

输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.
提示：

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    weight = total // 2
    dp = [False] * (weight+1)
    dp[0] = True
    for i in nums:
        for j in range(weight+1, nums[i]-1, -1):
            dp[j] = dp[j] or dp[j-nums[i]]
    return dp[weight]

