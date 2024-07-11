"""
给定一个字符串 s 和一个整数 k，从字符串开头算起, 每计数至 2k 个字符，就反转这 2k 个字符中的前 k 个字符。

如果剩余字符少于 k 个，则将剩余字符全部反转。

如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"
"""


def reverse(s, k):
    for start in range(0, len(s), 2*k):
        end = start + k
        s = s[:start] + s[start:end][::-1] + s[end:]
    return s


if __name__ == '__main__':
    print(reverse("abcdefg", 2))
