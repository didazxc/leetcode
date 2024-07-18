"""
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。

示例 1：

输入：cost = [10, 15, 20]
输出：15
解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。
示例 2：

输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出：6
解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。
"""


def climb_stairs0(cost):
    dp = [0]*(len(cost)+1)
    dp[0] = 0
    dp[1] = 0
    for i in range(2, len(cost)+1):
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    return dp[len(cost)]


def climb_stairs(cost):
    last2 = cost[0]
    last1 = cost[1]
    for i in range(2, len(cost)):
        cur = min(last2, last1) + cost[i]
        last2, last1 = last1, cur
    return min(last2, last1)


if __name__ == '__main__':
    print(climb_stairs([10, 15, 20]))
    print(climb_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
