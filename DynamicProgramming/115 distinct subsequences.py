"""
https://leetcode.com/problems/distinct-subsequences/

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

Input: s = "rabbbit", t = "rabbit"
Output: 3

Input: s = "babgbag", t = "bag"
Output: 5

Constraints:
    1 <= s.length, t.length <= 1000
    s and t consist of English letters.
"""


def numDistinct(s: str, t: str) -> int:
    """
    动态规划

    dp[i+1][j+1] := numDistinct(s[:i+1], t[:j+1])
    """

    length_s = len(s)
    length_t = len(t)
    if length_s < length_t:
        return 0
    dp = [[0 for _ in range(length_t+1)] for _ in range(length_s+1)]
    for i in range(length_s+1):
        dp[i][0] = 1
    for j in range(0, length_t):
        for i in range(j, length_s):
            # print(j, i)
            dp[i+1][j+1] = dp[i][j+1]
            if s[i] == t[j]:
                dp[i+1][j+1] += dp[i][j]
    return dp[length_s][length_t]


print(numDistinct(s="rabbb", t="rabb"))
print(numDistinct(s="rar", t="rar"))
print(numDistinct(s="rabbbit", t="rabbit"))
print(numDistinct(s="babgbag", t="bag"))
