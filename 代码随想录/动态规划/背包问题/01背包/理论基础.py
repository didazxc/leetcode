

def bag_problem1(weight: list, value: list, bagweight: int):
    dp = [[0]*(bagweight+1) for _ in range(len(weight))]

    for j in range(weight[0], bagweight+1):
        dp[0][j] = value[0]

    for j in range(bagweight+1):
        for i in range(1, len(weight)):
            if j < weight[i]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])

    return dp[len(weight) - 1][bagweight]


def bag_problem2(weight: list, value: list, bagweight: int):
    dp = [0] * (bagweight + 1)
    for row in range(len(weight)):
        for col in range(bagweight, weight[row] - 1, -1):
            dp[col] = max(dp[col], dp[col - weight[row]] + value[row])
    return dp[bagweight]


if __name__ == "__main__":

    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagweight = 4

    result = bag_problem2(weight, value, bagweight)
    print(result)

