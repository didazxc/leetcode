"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，能够偷窃到的最高金额。

示例 1：

输入：nums = [2,3,2]

输出：3

解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

示例 2：

输入：nums = [1,2,3,1]

输出：4

解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。偷窃到的最高金额 = 1 + 3 = 4 。

示例 3：

输入：nums = [0]

输出：0

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 1000
"""


def rob(nums):
    n = len(nums)
    pre_max = 0
    cur_max1 = 0
    for i in range(n-1):
        pre_max, cur_max1 = cur_max1, max(cur_max1, pre_max + nums[i])
    pre_max = 0
    cur_max2 = 0
    for i in range(1, n):
        pre_max, cur_max2 = cur_max2, max(cur_max2, pre_max + nums[i])
    return max(cur_max1, cur_max2)


if __name__ == '__main__':
    print(rob([1,2,3,1]))

