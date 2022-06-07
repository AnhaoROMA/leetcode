"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices
where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,4,3,1]
Output: 0
"""


# solution: 动态规划
# dp[i]表示前 i 天的最大收益。
# 状态转移方程为：
# dp[i] = max(
#               [i-1],
#               prices[i] - min(prices[:i])
#            )
def stock(prices: list[int]) -> int:
    length = len(prices)
    if length == 1:
        return 0
    dp = [0 for _ in range(length)]
    min_p = prices[0]
    for i in range(1, length):
        dp[i] = max(dp[i-1], prices[i]-min_p)
        min_p = min(min_p, prices[i])
    return dp[-1]
