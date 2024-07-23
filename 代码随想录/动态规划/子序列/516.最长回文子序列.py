"""
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。

示例 1: 输入: "bbbab" 输出: 4 一个可能的最长回文子序列为 "bbbb"。

示例 2: 输入:"cbbd" 输出: 2 一个可能的最长回文子序列为 "bb"。

提示：

1 <= s.length <= 1000
s 只包含小写英文字母
"""


def max_substr(s):
    dp = [[0]*len(s) for _ in s]

    for i in range(len(s)-1, -1, -1):
        for j in range(i, len(s)):
            if i == j:
                dp[i][j] = 1
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    return dp[0][-1]


if __name__ == '__main__':
    print(max_substr("bbbab"))
