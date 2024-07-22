"""
给两个整数数组 A 和 B ，返回两个数组中公共的、长度最长的子数组的长度。

示例：

输入：

A: [1,2,3,2,1]
B: [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3, 2, 1] 。
提示：

1 <= len(A), len(B) <= 1000
0 <= A[i], B[i] < 100
"""


def longest0(nums1, nums2):
    max_length = 0
    dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
    for i in range(1, len(nums1)+1):
        for j in range(1, len(nums2)+1):
            if nums1[i-1] == nums2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
                max_length = max(max_length, dp[i][j])
    return max_length


def longest(nums1, nums2):
    max_length = 0
    dp = [0] * (len(nums2)+1)
    for i in range(1, len(nums1)+1):
        for j in range(len(nums2), 0, -1):
            if nums1[i-1] == nums2[j-1]:
                dp[j] = dp[j-1]+1
                max_length = max(max_length, dp[j])
            else:
                dp[j] = 0
    return max_length


if __name__ == '__main__':
    print(longest([1,2,3,2,1], [3,2,1,4,7]))
