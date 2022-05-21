"""
https://leetcode.com/problems/coin-change/

You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1

Input: coins = [1], amount = 0
Output: 0
"""


def solution(coins: list[int], amount: int):
    result = [-1 for _ in range(amount+1)]
    result[0] = 0
    for i in range(amount+1):
        for choice in coins:
            if i - choice < 0:
                continue
            else:
                if result[i-choice] == -1:
                    result[i] = max(result[i], -1)
                else:
                    if result[i] == -1:
                        result[i] = 1 + result[i-choice]
                    else:
                        result[i] = min(result[i], 1 + result[i-choice])
    return result[-1]


a = [1, 2, 5]
b = 11
c = [2]
d = 5
e = 100
f = [411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422]
g = 9864
print(solution(a, b))
