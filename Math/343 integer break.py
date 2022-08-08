"""
https://leetcode.com/problems/integer-break/

Given an integer n,
break it into the sum of k positive integers,
where k >= 2,
and maximize the product of those integers.

Return the maximum product you can get.

Input: n = 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Input: n = 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
"""


def integer_break(n: int) -> int:
    dp = [0 for _ in range(n+1)]
    dp[1] = 1

    def helping_hand(x: int) -> int:
        if dp[x] == 0:
            dp[x] = max([i*max(helping_hand(x-i), x-i) for i in range(1, x)])
        return dp[x]

    return helping_hand(x=n)


print(integer_break(58))
