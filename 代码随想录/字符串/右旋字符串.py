"""
剑指Offer58-II.左旋转字符串
https://gitee.com/programmercarl/leetcode-master/blob/master/problems/%E5%89%91%E6%8C%87Offer58-II.%E5%B7%A6%E6%97%8B%E8%BD%AC%E5%AD%97%E7%AC%A6%E4%B8%B2.md


右旋字符串
力扣已经将剑指offer题目下架，所以在卡码网上给大家提供类似的题目来练习

卡码网题目链接

字符串的右旋转操作是把字符串尾部的若干个字符转移到字符串的前面。给定一个字符串 s 和一个正整数 k，请编写一个函数，将字符串中的后面 k 个字符移到字符串的前面，实现字符串的右旋转操作。

例如，对于输入字符串 "abcdefg" 和整数 2，函数应该将其转换为 "fgabcde"。

输入：输入共包含两行，第一行为一个正整数 k，代表右旋转的位数。第二行为字符串 s，代表需要旋转的字符串。

输出：输出共一行，为进行了右旋转操作后的字符串。

样例输入：

2
abcdefg
样例输出：

fgabcde
数据范围：1 <= k < 10000, 1 <= s.length < 10000;

"""


def rotate0(s, k):
    n = len(s)
    return s[n-k:]+s[:n-k]


def rotate(s: list, k: int):
    """
    向后平移k位
    """
    n = len(s)
    for i in range(k):
        tmp = s[n-1]
        for j in range(n-1, -1, -1):
            s[j] = s[j-1]
        s[0] = tmp
    return s


if __name__ == '__main__':
    print(rotate(list('abcdefg'), 2))
