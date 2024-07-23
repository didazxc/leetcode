"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""


def trap_col(height):
    return sum(min(max(height[:i+1]), max(height[i:])) - height[i] or 0 for i in range(1, len(height)-2))


def trap(height):
    s = 0
    st = []
    for i in range(len(height)):
        while st and height[i] > height[st[-1]]:
            bottom = st.pop()
            if st:
                h = min(height[i], height[st[-1]]) - height[bottom]
                w = i - st[-1] - 1
                s += h * w
        st.append(i)
    return s


if __name__ == '__main__':
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
