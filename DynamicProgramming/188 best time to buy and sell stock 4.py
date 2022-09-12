"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
"""


def stock(k: int, prices: list[int]) -> int:
    length = len(prices)
    # 如果 k 为 0 或者 prices[] 为空，则直接返回 0 。
    if k == 0 or length == 0:
        return 0
    # 如果 k 不小于 len(prices) 的一半，则说明我们可以进行无限次交易。
    if k >= length//2:
        max_profits = 0
        for i in range(1, length):
            if prices[i] > prices[i-1]:
                max_profits += prices[i]-prices[i-1]
        return max_profits
    # 否则，使用动态规划求解。

    # dp[i][j][k]
    #   ->  dp[ 天数 ][ 交易次数（买入时 +1） ][ 手中是否持股 ]
    dp = [
        [[0, 0] for _ in range(k+1)] for _ in range(length)
    ]
    # 状态转移方程：
    #   dp[i][j][0] = max( dp[i-1][j][0], dp[i-1][j][1]+prices[i] )
    #   dp[i][j][1] = max( dp[i-1][j][1], dp[i-1][j-1][0]-prices[i] )

    # 边界：i=0 时。
    for j in range(1, k+1):
        dp[0][j][0] = 0
        dp[0][j][1] = -1*prices[0]
    # 边界：j=0 时。
    for i in range(length):
        dp[i][0][0] = 0
        dp[i][0][1] = -1*10**9
    # 一般情况。
    for i in range(1, length):
        for j in range(1, k+1):
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1]+prices[i])
            dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]-prices[i])
    return dp[-1][-1][0]


print(stock(2, [2, 4, 1]))
