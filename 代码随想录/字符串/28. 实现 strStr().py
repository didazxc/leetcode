"""
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1: 输入: haystack = "hello", needle = "ll" 输出: 2

示例 2: 输入: haystack = "aaaaa", needle = "bba" 输出: -1

说明: 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


KMP算法：https://www.zhihu.com/question/34623343/answer/3149543139?utm_psn=1795038245349908480

文本串haystack中查找模式串needle时，文本串指针永不回头，对比失败时，模式串依靠next数组对齐到最长已对比前缀之后重新对比。

"""


def build_next(s, nxt):
    i = -2  # i = 前缀新增字符位置
    for j in range(-1, len(s)):  # j = 后缀新增字符的位置
        while i >= 0 and s[i] != s[j]:  # 令i可以等0，就可以同时判断第一个元素的相等性，后面就可以统一为i加1了
            i = nxt[i-1]  # nxt存放该后缀对应的最长前缀长度
        i += 1
        nxt[j] = i  # python list 索引具有循环特性，-1存在了最后一位，最终会被覆盖掉


def build_next1(s, nxt):
    nxt[0] = 0
    j = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = nxt[j-1]
        if s[i] == s[j]:
            j += 1
        nxt[i] = j


def strStr(haystack: str, needle: str):
    n = len(needle)
    if n == 0:
        return 0
    nxt = [0] * n
    build_next(needle, nxt)
    print(nxt)
    i = 0
    for c in range(len(haystack)):
        while i > 0 and haystack[c] != needle[i]:
            i = nxt[i-1]
        if haystack[c] == needle[i]:
            i += 1
        if i == n:
            return c - n + 1

    return -1


class Solution:
    def getNext(self, next, s: str) -> None:
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        print(next)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1


if __name__ == '__main__':
    print(strStr('aabdaafaabaabaaf', 'aabaaf'))
    print(Solution().strStr('aabdaafaabaabaaf', 'aabaaf'))

