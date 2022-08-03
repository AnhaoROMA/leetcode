"""
https://leetcode.com/problems/coin-change-2/

You are given an integer array coins
    representing coins of different denominations
and an integer amount
    representing a total amount of money.

Return the number of combinations that make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Input: amount = 10, coins = [10]
Output: 1

Constraints:
    1 <= coins.length <= 300
    1 <= coins[i] <= 5000
    All the values of coins are unique.
    0 <= amount <= 5000
"""


def coin_change(amount: int, coins: list[int]) -> int:
    # 我的第一想法是 DFS ，但是 TLE 了。
    # coins.sort()
    # result = 0
    # dfs = [
    #     [amount, coins[:]]
    # ]
    # while dfs:
    #     left, choices = dfs.pop()
    #     if left == 0:
    #         result += 1
    #     length = len(choices)
    #     for i in range(length):
    #         if choices[i] > left:
    #             break
    #         else:
    #             dfs.append(
    #                 [left-choices[i], choices[i:]]
    #             )
    # return result

    # 然后，我想到了 DP 。
    # 但是当时我忘记了一点，就是在 “找零钱” 的问题上， “3+2” 与 “2+3” 是一样的。
    # （这与 “跳格子” 问题是不一样的。）
    # dp = [0 for _ in range(amount+1)]
    # dp[0] = 1
    # for i in range(1, amount+1):
    #     for step in coins:
    #         if i-step >= 0:
    #             dp[i] += dp[i-step]
    # # print(dp)
    # return dp[amount]

    # 那怎么调整 DP 方法呢？
    # 看一下下面的代码吧。
    dp = [0 for _ in range(amount+1)] # 这一步没有变化
    dp[0] = 1                         # 这一步没有变化

    for coin in coins:
        for i in range(coin, amount+1):
            dp[i] += dp[i-coin]
    # 这一步到底妙在哪呢？
    # 与我一开始想到的 DFS 其实是一样的效果：也就是不要混着使用不同面值的钱币。
    # 在 coin:coins 这一步，
    # 意思是，在这、以及这之后，我们仅仅可以使用面值为 coin 的钱币。
    # 这样，就保证了，“不混着使用不同面值的钱币”。

    return dp[amount]                 # 这一步没有变化