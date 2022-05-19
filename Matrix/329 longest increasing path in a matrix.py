"""
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""

# solution:
# 动态规划


def dfs(matrix: list[list[int]], dp: list[list[int]], x: int, y: int) -> int:
    if dp[x][y] != 0:
        return dp[x][y]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    result = 1
    for option in directions:
        i = x + option[0]
        j = y + option[1]
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[x][y] >= matrix[i][j]:
            continue
        else:
            result = max(result, 1 + dfs(matrix, dp, i, j))
    dp[x][y] = result
    return result


def find(matrix: list[list[int]]) -> int:
    dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dp[i][j] = dfs(matrix, dp, i, j)

    result = 1
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if result < dp[i][j]:
                result = dp[i][j]
    return result


a = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]
b = [
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]
print(find(a))
