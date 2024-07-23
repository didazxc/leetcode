"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""


def largest_area(heights):
    s = 0
    st = []
    for i in range(len(heights)):
        while st and heights[st[-1]] > heights[i]:
            mid = st.pop()
            if st:
                h = heights[mid]
                w = i - st[-1] -1
                s = max(s, h * w)
        st.append(i)
    return s


if __name__ == '__main__':
    print(largest_area([2,1,5,6,2,3]))
