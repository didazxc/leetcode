"""
给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1：

输入：k = 2, prices = [2,4,1]

输出：2 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2。

示例 2：

输入：k = 2, prices = [3,2,6,5,0,3]

输出：7 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4。随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。

提示：

0 <= k <= 100
0 <= prices.length <= 1000
0 <= prices[i] <= 1000
"""


def stock(prices, k):
    dp = [0] + [-float('inf'), 0]*k
    for price in prices:
        for i in range(k):
            dp[2*i+1] = max(dp[2*i+1], dp[2*i] - price)
            dp[2*i+2] = max(dp[2*i+2], dp[2*i+1] + price)
    return dp[-1]


if __name__ == '__main__':
    print(stock([2,4,1], 2))
    print(stock([3,2,6,5,0,3], 2))
