"""
https://leetcode.com/problems/number-of-ways-to-reach-a-position-after-exactly-k-steps/

You are given two positive integers startPos and endPos.
Initially, you are standing at position startPos on an infinite number line.
With one step, you can move either one position to the left, or one position to the right.

Given a positive integer k,
return the number of different ways to reach the position endPos starting from startPos,
such that you perform exactly k steps.
Since the answer may be very large, return it modulo 10^9 + 7.

Two ways are considered different if the order of the steps made is not exactly the same.

Note that the number line includes negative integers.

Input:
    startPos = 1, endPos = 2, k = 3
Output:
    3
Explanation:
    We can reach position 2 from 1 in exactly 3 steps in three ways:
        1 -> 2 -> 3 -> 2.
        1 -> 2 -> 1 -> 2.
        1 -> 0 -> 1 -> 2.
    It can be proven that no other way is possible, so we return 3.

Input:
    startPos = 2, endPos = 5, k = 10
Output:
    0
Explanation:
    It is impossible to reach position 5 from position 2 in exactly 10 steps.

Constraints:
    1 <= startPos, endPos, k <= 1000
"""

import math


def numberOfWays(startPos: int, endPos: int, k: int) -> int:
    """
    不妨设 startPos < endPos ，
    则最少也需要 net_steps=endPos-startPos 步，
    此时的走法是 RR...RR （ net_steps 个 R ）。

    而此题允许有冗余的步。
    显然冗余的步数一定是偶数。

    而冗余的走法是向左走，即：
        RRL RLR LRR ...
    假设走法中含有 m 个 L 与 n 个 R ，则
        n - m = net_steps
        m + n = k
    所以共有 C_{k}^{m}==C_{k}^{n} 种走法。
    """
    net_steps = abs(startPos - endPos)
    if k < net_steps:
        return 0
    if (k - net_steps) % 2 == 1:
        return 0
    ans = math.comb(k, (k-net_steps)//2)
    return ans % (10**9 + 7)


print(numberOfWays(1, 2, 3))
