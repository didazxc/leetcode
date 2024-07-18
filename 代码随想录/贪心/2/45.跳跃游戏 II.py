"""
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。从下标为 0 跳到下标为 1 的位置，跳  1  步，然后跳  3  步到达数组的最后一个位置。
说明: 假设你总是可以到达数组的最后一个位置。
"""


def jump0(nums):
    cnt = 0
    cur = 0
    cover = nums[0]
    while cur < cover < len(nums)-1:
        arr = [(i+nums[i], i) for i in range(cur+1, cover)]
        cover, cur = max(arr, key=lambda x: x[0])
        cnt += 1
    return cnt + 1


def jump(nums):
    cnt = 0
    cur_cover = 0
    next_cover = cur_cover
    for i in range(len(nums)-1):
        next_cover = max(i+nums[i], next_cover)
        if i == cur_cover:
            cur_cover = next_cover
            cnt += 1
    return cnt


if __name__ == '__main__':
    print(jump([2,3,1,1,4]))

