"""
https://leetcode.com/problems/out-of-boundary-paths/

There is an m x n grid with a ball.
The ball is initially at the position [startRow, startColumn].
You are allowed to move the ball to one of the four adjacent cells in the grid
(possibly out of the grid crossing the grid boundary).
You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn,
return the number of paths to move the ball out of the grid boundary.
Since the answer can be very large, return it modulo 10^9 + 7.

Constraints:
    1 <= m, n <= 50
    0 <= maxMove <= 50
    0 <= startRow < m
    0 <= startColumn < n
"""


# solution:
# 三维动态规划
# (1) dp[t][i][j]: 在位置 (i, j) 走 t 步 ”正好“ 出界的走法数；
# (2) dp[t][i][j] = dp[t-1][i+1][j] + dp[t-1][i-1][j] + dp[t-1][i][j+1] + dp[t-1][i][j-1]
def find_paths(m: int, n: int, max_move: int, start_row: int, start_column: int) -> int:
    dp = [
        [[0 for _ in range(n+2)] for _ in range(m+2)] for _ in range(max_move+1)
    ]

    # 初始化：当 max_move 为 0 时。
    t = 0
    for i in range(m+2):
        dp[t][i][0] = 1
        dp[t][i][n+1] = 1
    for j in range(n+1):
        dp[t][0][j] = 1
        dp[t][m+1][j] = 1

    # 开始动态规划
    t = 1
    while t <= max_move:
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[t][i][j] =\
                    dp[t-1][i+1][j] + dp[t-1][i-1][j] + dp[t-1][i][j+1] + dp[t-1][i][j-1]
        t += 1

    ans = 0
    for t in range(max_move+1):
        ans += dp[t][start_row+1][start_column+1]
    return ans % (10**9+7)


print(find_paths(m=2, n=3, max_move=2, start_row=0, start_column=0))
print(find_paths(m=2, n=2, max_move=2, start_row=0, start_column=0))
