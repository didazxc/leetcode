"""
给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。

示例 1:

输入: "abab"
输出: True
解释: 可由子字符串 "ab" 重复两次构成。
示例 2:

输入: "aba"
输出: False
示例 3:

输入: "abcabcabcabc"
输出: True
解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
"""


def get_next(s):
    nxt = [0]*len(s)
    i = -2
    for j in range(-1, len(s)):
        while i >= 0 and s[i] != s[j]:
            i = nxt[i-1]
        i += 1
        nxt[j] = i
    return nxt


def repeat(s):
    n = len(s)
    if n < 2:
        return False
    nxt = get_next(s)
    print(nxt)
    return nxt[-1] > 0 and n % (n - nxt[-1]) == 0


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        print(nxt)
        if nxt[-1] != -1 and len(s) % (len(s) - (nxt[-1] + 1)) == 0:
            return True
        return False

    def getNext(self, nxt, s):
        nxt[0] = -1
        j = -1
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j + 1]:
                j = nxt[j]
            if s[i] == s[j + 1]:
                j += 1
            nxt[i] = j
        return nxt


if __name__ == '__main__':
    print(repeat('abcabcabcabd'))
    print(Solution().repeatedSubstringPattern('abcabcabcabd'))

