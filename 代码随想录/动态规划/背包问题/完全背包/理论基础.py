def complete_pack(weight, value, bagWeight):
    dp = [0] * (bagWeight + 1)
    for i in range(len(weight)):  # 遍历物品
        for j in range(weight[i], bagWeight + 1):  # 遍历背包容量
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])
    return dp[bagWeight]


if __name__ == "__main__":
    weight = [1, 3, 4]
    value = [15, 20, 30]
    bagWeight = 4
    result = complete_pack(weight, value, bagWeight)
    print(result)
