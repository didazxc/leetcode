"""
给你两个字符串 s 和 t ，统计并返回在 s 的 子序列 中 t 出现的个数，结果需要对 10^9 + 7 取模。

示例 1：

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
 有 3 种可以从 s 中得到 "rabbit" 的方案。

示例 2：

输入：s = "babgbag", t = "bag"
输出：5
解释：
有 5 种可以从 s 中得到 "bag" 的方案。 

提示：

1 <= s.length, t.length <= 1000
s 和 t 由英文字母组成
"""


def diff_sub_lis(s, t):
    dp = [[0]* (len(s)+1) for _ in range(len(t)+1)]
    for j in range(len(s)+1):
        dp[0][j] = 1
    for i in range(1, len(t)+1):
        for j in range(1, len(s)+1):
            if s[j-1] == t[i-1]:
                dp[i][j] = dp[i-1][j-1] + dp[i][j-1]  # 将i和j对应起来是dp[i-1][j-1]个，不对应起来，就是dp[i][j-1]个
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]


if __name__ == '__main__':
    print(diff_sub_lis(s = "rabbbit", t = "rabbit"))
    print(diff_sub_lis(s = "babgbag", t = "bag"))
