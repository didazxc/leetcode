"""
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例：

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
"""


def min_distance0(word1, word2):
    dp = [[1]*(len(word2)+1) for _ in range(len(word1)+1)]
    dp[0][0] = 0
    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1)
    return dp[-1][-1]


def min_distance(word1, word2):
    dp = [[0]*(len(word2)+1) for _ in range(len(word1)+1)]
    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return len(word1) + len(word2) - 2 * dp[-1][-1]


if __name__ == '__main__':
    print(min_distance("sea", "eat"))

