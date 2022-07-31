"""
https://leetcode.com/problems/perfect-squares/

Given an integer n,
return the least number of perfect square numbers that sum to n.

A perfect square is an integer
    that is the square of an integer; in other words,
it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
    1 <= n <= 10^4
"""


def perfect_squares(n: int) -> int:
    """
    动态规划
    dp[i] := perfect_squares(i)
    dp[i] = min(
            1 + dp[i-1],
            1 + dp[i-4],
            1 + dp[i-9],
            ...
        )
    """
    dp = [0 for _ in range(n+1)]
    for i in range(1, n+1):
        max_step = int(i ** 0.5)
        dp[i] = 1 + min([dp[i - (j+1)*(j+1)] for j in range(max_step)])
    return dp[n]


print(perfect_squares(13))
