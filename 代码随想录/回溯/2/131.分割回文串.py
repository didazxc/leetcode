"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例: 输入: "aab" 输出: [ ["aa","b"], ["a","a","b"] ]
"""


def palindrome_track(raw_str, start_index, path, res):
    if start_index >= len(raw_str):
        res.append(path[:])
        return
    for i in range(start_index, len(raw_str)):
        s = raw_str[start_index:i+1]
        if all(s[k] == s[len(s)-k-1] for k in range(len(s)//2)):
            path.append(s)
            palindrome_track(raw_str, i + 1, path, res)
            path.pop()


def palindrome(raw_str):
    res = []
    palindrome_track(raw_str, 0, [], res)
    return res


if __name__ == '__main__':
    print(palindrome("aab"))
