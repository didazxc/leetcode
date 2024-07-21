"""
有N种物品和一个容量为V 的背包。第i种物品最多有Mi件可用，每件耗费的空间是Ci ，价值是Wi 。求解将哪些物品装入背包可使这些物品的耗费的空间 总和不超过背包容量，且价值总和最大。

多重背包和01背包是非常像的， 为什么和01背包像呢？

每件物品最多有Mi件可用，把Mi件摊开，其实就是一个01背包问题了。
"""


def bag_problem1(weight: list, value: list, bagweight: int, counts: list):
    new_weight = []
    new_value = []
    for w, v, c in zip(weight, value, counts):
        for _ in range(c):
            new_weight.append(w)
            new_value.append(v)
    dp = [0] * (bagweight + 1)
    for row in range(len(new_weight)):
        for col in range(bagweight, new_weight[row] - 1, -1):
            dp[col] = max(dp[col], dp[col - new_weight[row]] + new_value[row])
            print(row, col, dp)
    return dp[bagweight]


def bag_problem2(weight: list, value: list, bagweight: int, counts: list):
    dp = [0] * (bagweight + 1)
    for row in range(len(weight)):
        for col in range(bagweight, weight[row] - 1, -1):
            for k in range(1, counts[row]+1):
                if col - k*weight[row] >= 0:
                    dp[col] = max(dp[col], dp[col - k*weight[row]] + k*value[row])
                print(row, col, k, dp)
    return dp[bagweight]


if __name__ == "__main__":

    weight = [1, 3, 4]
    value = [15, 20, 30]
    counts = [4, 1, 1]
    bagweight = 4

    result = bag_problem2(weight, value, bagweight, counts)
    print(result)
