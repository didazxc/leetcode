"""
给定一个非负整数 N，找出小于或等于 N 的最大的整数，同时这个整数需要满足其各个位数上的数字是单调递增。

（当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。）

示例 1:

输入: N = 10
输出: 9
示例 2:

输入: N = 1234
输出: 1234
示例 3:

输入: N = 332
输出: 299
说明: N 是在 [0, 10^9] 范围内的一个整数。
"""


def increase_num(num):
    num_arr = [int(i) for i in str(num)]
    flag = 0
    for i in range(len(num_arr)-1, 0, -1):
        if num_arr[i-1] > num_arr[i]:
            num_arr[i - 1] -= 1
            flag = i
    for i in range(flag, len(num_arr)):
        num_arr[i] = 9
    return ''.join(str(i) for i in num_arr)


if __name__ == '__main__':
    print(increase_num(332))
