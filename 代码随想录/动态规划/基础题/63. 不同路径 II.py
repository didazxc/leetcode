"""
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

示例 1：



输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2 解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
向右 -> 向右 -> 向下 -> 向下
向下 -> 向下 -> 向右 -> 向右
示例 2：



输入：obstacleGrid = [[0,1],[0,0]]
输出：1
提示：

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] 为 0 或 1
"""


def steps(obstacle_grid):
    if obstacle_grid[0][0] == 1 or obstacle_grid[-1][-1] == 1:
        return 0
    n = len(obstacle_grid[0])
    dp = [0]*n
    for i in range(n):
        if obstacle_grid[0][i] == 1:
            break
        dp[i] = 1
    m = len(obstacle_grid)
    for row in range(1, m):
        for i in range(n):
            if obstacle_grid[row][i] == 1:
                dp[i] = 0
            elif i > 0:
                dp[i] += dp[i-1]
    return dp[-1]


if __name__ == '__main__':
    print(steps([[0,0,0],[0,1,0],[0,0,0]]))
