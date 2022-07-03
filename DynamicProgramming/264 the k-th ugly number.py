"""
https://leetcode.com/problems/ugly-number-ii/
"""


# Use Dynamic Programming.
#
# Since every ugly number is from one of previous ugly number time 2 or 3 or 5.
# We need i2, i3 and i5 three pointers to point the three ugly numbers
# from previous ugly numbers that times 2, 3, 5.
#
# We iterate the ugly number list and we want to find
# the min(i2 x 2, i3 x 3 and i5 x 5)
# this will give us the current ugly number for index i.
#
# If the current ugly number is from 2 x i2 then we update i2,
# if it is from 3 x i3 we update i3
# and if it is from 5 x i5 then we update i5.
def nthUglyNumber(n: int) -> int:
    dp = [1] * (n + 1)
    index2, index3, index5 = 1, 1, 1
    for i in range(2, n + 1):
        dp[i] = min(2 * dp[index2], 3 * dp[index3], 5 * dp[index5])
        if dp[i] == 2 * dp[index2]: index2 += 1
        if dp[i] == 3 * dp[index3]: index3 += 1
        if dp[i] == 5 * dp[index5]: index5 += 1
    return dp[-1]
