"""
https://leetcode.com/problems/maximal-square/

Given an m x n binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.
"""


# 动态规划
# dp[i][j] 为子问题 “以 (i, j) 为右下角的 子矩阵 的 maximal-square 的最大面积”
# 如果 matrix[i][j] == "0"，则 dp[i][j] = 0
# 如果 matrix[i][j] == "1"，则 dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
def find(matrix: list[list[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])
    ans = 0
    dp = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == "1":
                if i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = 1
                ans = max(ans, dp[i][j])
            else:
                dp[i][j] = 0
    # print(dp)
    return ans*ans


print(
    find(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
    )
)
