"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释:  连续子数组  [4,-1,2,1] 的和最大，为  6。
"""


def max_sub0(nums):
    result = -float('inf')
    s = 0
    for i in nums:
        s += i
        if s > result:
            result = s
        if s < 0:
            s = 0
    return result


def max_sub(nums):
    dp = [nums[0]]
    for i in range(1, len(nums)):
        dp.append(max(dp[i-1]+nums[i], nums[i]))
    return max(dp)


if __name__ == '__main__':
    print(max_sub([-2,1,-3,4,-1,2,1,-5,4]))
