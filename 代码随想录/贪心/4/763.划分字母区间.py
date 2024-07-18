"""
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

示例：

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8] 解释： 划分结果为 "ababcbaca", "defegde", "hijhklij"。 每个字母最多出现在一个片段中。 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
提示：

S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。
"""


def split(s):
    chars = [0]*26
    for i in range(len(s)):
        chars[ord(s[i]) - ord('a')] = i
    start = 0
    end = 0
    res = []
    for i in range(len(s)):
        end = max(end, chars[ord(s[i]) - ord('a')])
        if i == end:
            res.append(end - start + 1)
            start = i + 1
    return res


if __name__ == '__main__':
    print(split("ababcbacadefegdehijhklij"))
