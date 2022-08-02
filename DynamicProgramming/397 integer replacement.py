"""
https://leetcode.com/problems/integer-replacement/

Given a positive integer n, you can apply one of the following operations:
    If n is even, replace n with n / 2.
    If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
    or 7 -> 6 -> 3 -> 2 -> 1

Input: n = 4
Output: 2

Constraints:
    1 <= n <= 2^{31}-1
"""


class Solution:
    def integerReplacement(self, n: int) -> int:
        """
        本题使用 DP 或者带记忆的递归会失败，报 “Memory Limit Exceeded” 。

        而使用不带记忆的递归则会成功。

        原因在于，一般我们使用 DP 或者带记忆的递归，目的在于 “不做重复的工作”。
        但是，在这里，我们不可能会做重复的工作。
        为什么呢？
        因为：
            n 在不断变小          ， n 为偶数；
            (n+1)//2 != (n-1)//2， n 为奇数
        """
        # dp = [-1 for _ in range(n+2)]
        # """
        #     0 1 2 3 4 5 6 7 8 9 ... n-1 n n+1
        # """
        # dp[1] = 0
        #
        # def cal(m: int) -> int:
        #     if dp[m] != -1:
        #         return dp[m]
        #     if m % 2 == 0:
        #         tmp_res = 1 + cal(m//2)
        #         dp[m] = tmp_res
        #         return tmp_res
        #     else:
        #         tmp_res = 1 + min(cal(m+1), cal(m-1))
        #         dp[m] = tmp_res
        #         return tmp_res
        #
        # return cal(n)

        if n == 1:
            return 0
        if n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n + 1), self.integerReplacement(n - 1))
