"""
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
提示：输入的字符串长度不会超过 1000 。
"""


def extend(word, i, j):
    res = 0
    while i>=0 and j<len(word) and word[i] == word[j]:
        res += 1
        i -= 1
        j += 1
    return res


def count_substring0(word):
    res = 0
    for i in range(len(word)):
        res += extend(word, i, i)
        res += extend(word, i, i+1)
    return res


def count_substring(word):
    cnt = 0
    dp = [[False] * len(word) for _ in word]
    for i in range(len(word)-1, -1, -1):
        for j in range(i, len(word)):
            if word[i] == word[j] and (j - i <= 1 or dp[i+1][j-1]):
                dp[i][j] = True
            cnt += 1
    return cnt


if __name__ == '__main__':
    print(count_substring("aaa"))
