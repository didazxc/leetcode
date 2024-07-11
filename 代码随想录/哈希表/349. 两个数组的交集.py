"""
给定两个数组，编写一个函数来计算它们的交集。

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

res = [2]

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

说明： 输出结果中的每个元素一定是唯一的。 我们可以不考虑输出结果的顺序。
"""


def intersect1(nums1, nums2):
    arr1 = [0]*1000
    for i in nums1:
        arr1[i - 1] = 1
    arr2 = [0] * 1000
    for i in nums2:
        arr2[i - 1] = 1
    res = []
    for i in range(1000):
        if arr1[i] == 1 and arr2[i] == 1:
            res.append(i + 1)
    return res


def intersect(nums1, nums2):
    return list(set(nums1) & set(nums2))


if __name__ == '__main__':
    print(intersect([1, 2, 2, 1], [2, 2]))

