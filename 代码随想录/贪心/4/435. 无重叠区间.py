"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意: 可以认为区间的终点总是大于它的起点。 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

示例 1:

输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。
示例 2:

输入: [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
示例 3:

输入: [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
"""


def overlap0(intervals):
    intervals.sort(key=lambda x: x[0])
    min_end = -float('inf')
    total = 0
    cnt = 0
    for start, end in intervals:
        if start >= min_end:
            total += cnt
            cnt = 0
            min_end = end
        else:
            cnt += 1
            min_end = min(min_end, end)
    total += cnt
    return total


def overlap(intervals):
    intervals.sort(key=lambda x: x[0])
    cnt = 1
    for i in range(1, len(intervals)):
        if intervals[i][0] >= intervals[i-1][1]:
            cnt += 1
        else:
            intervals[i][1] = min(intervals[i][1], intervals[i-1][0])
    return len(intervals) - cnt


if __name__ == '__main__':
    print(overlap([ [1,2], [2,3], [3,4], [1,3] ]))
