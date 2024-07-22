"""
我们在两条独立的水平线上按给定的顺序写下 A 和 B 中的整数。

现在，我们可以绘制一些连接两个数字 A[i] 和 B[j] 的直线，只要 A[i] == B[j]，且我们绘制的直线不与任何其他连线（非水平线）相交。

以这种方法绘制线条，并返回我们可以绘制的最大连线数。

1035.不相交的线
"""


def max_uncross(nums1, nums2):
    dp = [0] * (len(nums2) + 1)
    for i in range(1, len(nums1)+1):
        for j in range(1, len(nums2)+1):
            if nums1[i-1] == nums2[j-1]:
                dp[j] = dp[j-1] + 1
            else:
                dp[j] = max(dp[j], dp[j-1])
    return dp[-1]


if __name__ == '__main__':
    print(max_uncross([2,5,1,2,5], [10,5,2,1,5,2]))
