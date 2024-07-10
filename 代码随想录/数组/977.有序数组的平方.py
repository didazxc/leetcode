"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]，排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
"""


def power(arr):
    res = [0]*len(arr)
    k = len(arr) - 1
    s = 0
    e = len(arr) - 1
    while e >= s:
        ss = arr[s] * arr[s]
        ee = arr[e] * arr[e]
        if ee >= ss:
            res[k] = ee
            e -= 1
        else:
            res[k] = ss
            s += 1
        k -= 1
    return res


if __name__ == '__main__':
    print(power([-7, -3, 2, 3, 11]))
