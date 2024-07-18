"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:
输入3，输出5
"""


def num_trees(n: int) -> int:
    dp = [1] * (n+1)
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] += dp[j-1]*dp[i-j]
    return dp[n]



