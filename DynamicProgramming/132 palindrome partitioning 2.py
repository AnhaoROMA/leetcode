"""
https://leetcode.com/problems/palindrome-partitioning-ii/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase English letters only.
"""


def minCut(s: str) -> int:
    n = len(s)

    # dp[i] := minCut(s[:i+1])
    dp = [-1 for _ in range(n)]

    dp[0] = 0
    for i in range(1, n):
        if s[:i+1] == s[:i+1][::-1]:
            dp[i] = 0
        else:
            ans = 2000
            for j in range(i):
                # s[:i+1] = s[:j+1] + s[j+1:i+1]
                if s[j+1:i+1] == s[j+1:i+1][::-1]:
                    ans = min(ans, dp[j] + 1)
            dp[i] = ans
    return dp[n-1]


print(minCut("a"))
