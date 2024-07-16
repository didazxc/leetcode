"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""

letters = [
            "",     # 0
            "",     # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs", # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]


def combine_nums(nums, index, s, res):
    if len(s) == len(nums):
        res.append(s)
        return
    for i in letters[int(nums[index])]:
        combine_nums(nums, index + 1, s+i, res)


def combine(nums):
    res = []
    combine_nums(nums, 0, '', res)
    return res


if __name__ == '__main__':
    print(combine("23"))
