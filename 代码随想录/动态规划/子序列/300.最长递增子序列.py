"""
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

示例 1：

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
示例 2：

输入：nums = [0,1,0,3,2,3]
输出：4
示例 3：

输入：nums = [7,7,7,7,7,7,7]
输出：1
提示：

1 <= nums.length <= 2500
-10^4 <= nums[i] <= 104
"""


def length_lis0(nums):
    if len(nums) <= 0:
        return 0
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(dp)
    return max(dp)


def length_lis(nums):
    tails = [nums[0]]
    for num in nums[1:]:
        if num > tails[-1]:
            tails.append(num)
        else:
            left = 0
            right = len(tails) - 1
            while left < right:
                mid = (left+right)//2
                if num > tails[mid]:
                    left = mid + 1
                elif num < tails[mid]:
                    right = mid - 1
                else:
                    left = mid
                    break
            tails[left] = num
    return len(tails)


if __name__ == '__main__':
    print(length_lis([10,9,2,5,3,7,101,3]))
