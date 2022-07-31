"""
https://leetcode.com/problems/interleaving-string/

Given strings s1, s2, and s3,
find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration
where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is
    s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Input: s1 = "", s2 = "", s3 = ""
Output: true
"""


# TLE: DFS
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dfs = list()
        dfs.append(
            [
                s1, s2, s3
            ]
        )
        while dfs:
            temp_s1, temp_s2, temp_s3 = dfs.pop()
            if len(temp_s3) == 0:
                if len(temp_s1) == 0 and len(temp_s2) == 0:
                    return True
                else:
                    return False
            if len(temp_s1) > 0 and temp_s1[0] == temp_s3[0]:
                dfs.append(
                    [
                        temp_s1[1:], temp_s2, temp_s3[1:]
                    ]
                )
            if len(temp_s2) > 0 and temp_s2[0] == temp_s3[0]:
                dfs.append(
                    [
                        temp_s1, temp_s2[1:], temp_s3[1:]
                    ]
                )
        return False


# solution：动态规划
# 我们定义一个 boolean 二维数组 dp[i][j] 来表示 s1[0, i) 和 s2[0, j） 组合后能否构成 s3[0, i+j)
# 状态转换方程也很好写了
# 如果 dp[i-1][j] == true，并且 s1[i-1] == s3[i+j-1]， dp[i][j] = true
# 如果 dp[i][j-1] == true，并且 s2[j-1] == s3[i+j-1]， dp[i][j] = true
# 否则的话，就更新为 dp[i][j] = false
def solution(s1: str, s2: str, s3: str) -> bool:
    length_1 = len(s1)
    length_2 = len(s2)
    if len(s3) != length_1+length_2:
        return False
    dp = [[False for _ in range(length_2+1)] for _ in range(length_1+1)]
    dp[0][0] = True
    for i in range(1, length_1+1):
        dp[i][0] = (s1[:i] == s3[:i])
    for j in range(1, length_2+1):
        dp[0][j] = (s2[:j] == s3[:j])
    for i in range(1, length_1+1):
        for j in range(1, length_2+1):
            if dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                dp[i][j] = True
            elif dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                dp[i][j] = True
            else:
                dp[i][j] = False
    return dp[-1][-1]


print(solution("aabcc", "dbbca", "aadbbcbcac"))
