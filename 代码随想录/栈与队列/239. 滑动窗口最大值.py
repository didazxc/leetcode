"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回滑动窗口中的最大值。

进阶：

你能在线性时间复杂度内解决此题吗？



提示：

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
"""
from collections import deque


def window(nums, k):
    res = []
    queue = deque()
    for i in range(len(nums)):
        while queue and queue[-1] <= nums[i]:
            queue.pop()
        queue.append(i)
        if i >= k-1:
            if queue[0] <= i - k:
                queue.popleft()
            res.append(nums[queue[0]])
    return res


if __name__ == '__main__':
    print(window([1,3,-1,-3,5,3,6,7],3))
