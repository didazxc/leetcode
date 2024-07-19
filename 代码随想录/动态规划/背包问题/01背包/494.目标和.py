"""
难度：中等

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
一共有5种方法让最终目标和为3。

提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。
"""


def target_sum_ways1(nums, target):
    if sum(nums) < abs(target):
        return 0
    if (sum(nums) - abs(target)) % 2 == 1:
        return 0
    weight = (sum(nums) - abs(target)) // 2
    dp = [0] * (weight + 1)
    dp[0] = 1
    for num in nums:
        for j in range(weight, num-1, -1):
            dp[j] = dp[j] + dp[j-num]
    return dp[-1]


def target_sum_ways2(nums, target):
    if sum(nums) < abs(target):
        return 0
    if (sum(nums) - abs(target)) % 2 == 1:
        return 0
    weight = (sum(nums) - abs(target)) // 2
    dp = [[0] * (weight + 1) for _ in range(len(nums))]
    dp[0][0] = 1
    dp[0][nums[0]] = 1
    for i in range(1, len(nums)):
        for j in range(weight + 1):
            if j < nums[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
    return dp[-1][-1]


if __name__ == '__main__':
    print(target_sum_ways2([1, 1, 1, 1, 1], 3))
