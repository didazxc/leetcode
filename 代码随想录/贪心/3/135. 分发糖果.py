"""
老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。

你需要按照以下要求，帮助老师给这些孩子分发糖果：

每个孩子至少分配到 1 个糖果。
相邻的孩子中，评分高的孩子必须获得更多的糖果。
那么这样下来，老师至少需要准备多少颗糖果呢？

示例 1:

输入: [1,0,2]
输出: 5
解释: 你可以分别给这三个孩子分发 2、1、2 颗糖果。
示例 2:

输入: [1,2,2]
输出: 4
解释: 你可以分别给这三个孩子分发 1、2、1 颗糖果。第三个孩子只得到 1 颗糖果，这已满足上述两个条件。
"""


def candy0(nums):
    cnt = 1
    bigger_cnt = 0
    smaller_cnt = 0
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            bigger_cnt = 0
            smaller_cnt = 0
            cnt += 1
        if nums[i] > nums[i-1]:
            bigger_cnt += 1
            smaller_cnt = 0
            cnt += bigger_cnt + 1
        elif nums[i] < nums[i-1]:
            bigger_cnt = 0
            smaller_cnt += 1
            cnt += smaller_cnt + 1
    return cnt


def candy(nums):
    vec = [1]*len(nums)
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            vec[i] = vec[i-1]+1
    for i in range(len(nums)-2, -1, -1):
        if nums[i] > nums[i+1]:
            vec[i] = max(vec[i], vec[i+1]+1)
    return sum(vec)


if __name__ == '__main__':
    print(candy([1,2,2]))
