"""
https://leetcode.com/problems/delete-operation-for-two-strings/

Given two strings word1 and word2,
return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

Input:
word1 = "sea", word2 = "eat"
Output:
2
Explanation:
You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Input:
word1 = "leetcode", word2 = "etco"
Output:
4
"""


# solution:
# 给定两个字符串，每一步允许从其中任意一个字符串里删去一个字符。问至少删多少次可以使得两个字符串变得一样。
#
# 对于一个字符串来说，删掉其某个字符后得到的剩余串一定是原串的子序列，
# 所以这道题相当于问两个串的最长公共子序列的长度是多少。
def max_subsequence_length(a: str, b: str) -> int:
    """
    求最长公共子序列的长度
    """

    # 动态规划最重要的一步：
    # 《 DP表的意义 》
    # dp[i][j] 表示 a[:i] 与 b[:j] 的最长公共子序列的长度。
    #
    # 动态规划最核心的一步：
    # 《 状态转移方程 》
    # 本题的状态转移方程见代码部分。
    m = len(a)
    n = len(b)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[-1][-1]


def solution(string_1: str, string_2: str) -> int:
    length = max_subsequence_length(string_1, string_2)
    return len(string_1) - length + len(string_2) - length


print(solution("sea", "eat"))
