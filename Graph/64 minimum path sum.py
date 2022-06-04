"""
https://leetcode.com/problems/minimum-path-sum/

Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right,
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""


# 本题可以使用DFS，但是更好的方法应该是DP。
# DP[i][j]表示从(i, j)点走到终点的最短路径。
# 状态转移方程为 DP[i][j] = grid[i][j] + min(DP[i+1][j], DP[i][j+1])
def min_path(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    i = m - 1
    for j in range(n-1, -1, -1):
        dp[i][j] = grid[i][j] + dp[i][j+1]

    j = n - 1
    for i in range(m-1, -1, -1):
        dp[i][j] = grid[i][j] + dp[i+1][j]

    for i in range(m-2, -1, -1):
        for j in range(n-2, -1, -1):
            dp[i][j] = grid[i][j] + min(dp[i+1][j], dp[i][j+1])

    return dp[0][0]


a = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
b = [
    [1, 2, 3],
    [4, 5, 6]
]
print(min_path(b))
