"""
在象棋中，马和象的移动规则分别是“马走日”和“象走田”。现给定骑士的起始坐标和目标坐标，要求根据骑士的移动规则，计算从起点到达目标点所需的最短步数。

骑士移动规则如图，红色是起始位置，黄色是骑士可以走的地方。



棋盘大小 1000 x 1000（棋盘的 x 和 y 坐标均在 [1, 1000] 区间内，包含边界）

输入描述

第一行包含一个整数 n，表示测试用例的数量。

接下来的 n 行，每行包含四个整数 a1, a2, b1, b2，分别表示骑士的起始位置 (a1, a2) 和目标位置 (b1, b2)。

输出描述

输出共 n 行，每行输出一个整数，表示骑士从起点到目标点的最短路径长度。

输入示例

6
5 2 5 4
1 1 2 2
1 1 8 8
1 1 8 7
2 1 3 3
4 6 4 6
输出示例

2
4
6
5
1
0
"""
from collections import deque
import heapq


def bfs(start, end):
    direct = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
    st = deque([start])
    moves = [[0] * (1000 + 1) for _ in range(1000 + 1)]
    while st:
        x, y = st.popleft()
        if x == end[0] and y == end[1]:
            break
        for dx, dy in direct:
            m_x, m_y = x + dx, y + dy
            if 1 <= m_x <= 1000 and 1 <= m_y <= 1000 and not moves[m_x][m_y]:
                moves[m_x][y + dy] = moves[x][y] + 1
                if m_x == end[0] and m_y == end[1]:
                    return moves[m_x][m_y]
                st.append((m_x, m_y))
    return moves[end[0]][end[1]]


class Point:
    def __init__(self, x, y, g, h):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __le__(self, other):
        return self.f < other.f

    def __lt__(self, other):
        return self.f <= other.f

    @staticmethod
    def distinct(x, y, end_x, end_y):
        return (x - end_x)**2 + (y - end_y)**2

    def generate(self, end_x, end_y, moves):
        direct = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        for dx, dy in direct:
            x, y = self.x + dx, self.y + dy
            if 1 <= x <= 1000 and 1 <= y <= 1000 and not moves[x][y]:
                g = self.g + self.distinct(0, 0, dx, dy)
                h = self.distinct(x, y, end_x, end_y)
                moves[x][y] = moves[self.x][self.y] + 1
                yield Point(x, y, g, h)


def a_star(start_x, start_y, end_x, end_y):
    h = [Point(start_x, start_y, 0, Point.distinct(start_x, start_y, end_x, end_y))]
    moves = [[0] * (1000 + 1) for _ in range(1000 + 1)]
    while h:
        point = heapq.heappop(h)
        if point.x == end_x and point.y == end_y:
            break
        for next_point in point.generate(end_x, end_y, moves):
            if next_point.x == end_x and next_point.y == end_y:
                return moves[end_x][end_y]
            heapq.heappush(h, next_point)
    return moves[end_x][end_y]


if __name__ == '__main__':
    inputs = """
6
5 2 5 4
1 1 2 2
1 1 8 8
1 1 8 7
2 1 3 3
4 6 4 6
    """
    arr = [list(map(int, line.strip().split())) for line in inputs.strip().split('\n')]
    n = arr[0][0]
    for s_x, s_y, e_x, e_y in arr[1:]:
        print(a_star(s_x, s_y, e_x, e_y))

