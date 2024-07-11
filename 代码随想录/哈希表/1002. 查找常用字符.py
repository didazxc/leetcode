"""
给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），并以数组形式返回。你可以按 任意顺序 返回答案。

示例 1：

输入：words = ["bella","label","roller"] 输出：["e","l","l"]

示例 2：

输入：words = ["cool","lock","cook"] 输出：["c","o"]

提示：

1 <= words.length <= 100 1 <= words[i].length <= 100 words[i] 由小写英文字母组成
"""


def freq_chars(words):
    arr = [0 for _ in range(26)]
    for i in words[0]:
        arr[ord(i) - ord('a')] += 1
    for word in words[1:]:
        arr2 = [0 for _ in range(26)]
        for i in word:
            arr2[ord(i) - ord('a')] += 1
        for k in range(26):
            arr[k] = min(arr[k], arr2[k])
    res = []
    for k in range(26):
        for _ in range(arr[k]):
            res.append(chr(k + ord('a')))
    return res


if __name__ == '__main__':
    print(freq_chars(["bella", "label", "roller"]))
