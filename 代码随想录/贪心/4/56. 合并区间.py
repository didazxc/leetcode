"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: intervals = [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: intervals = [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
注意：输入类型已于2019年4月15日更改。 请重置默认代码定义以获取新方法签名。
"""


def merge(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]
    index = 0
    for i in range(1, len(intervals)):
        if intervals[i][0] <= res[index][1]:
            res[index][1] = max(res[index][1], intervals[i][1])
        else:
            res.append(intervals[i])
    return res


if __name__ == '__main__':
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
