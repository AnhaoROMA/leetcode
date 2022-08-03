"""
https://leetcode.com/problems/knight-probability-in-chessboard/
"""


def knight_probability(n: int, k: int, row: int, column: int) -> float:
    """
    三维 DP + 运用概率论中的加法公式与乘法公式。
    """
    directions = [
        (-1, -2), (-2, -1), (-2, 1), (-1, 2),
        (1, -2), (2, -1), (2, 1), (1, 2)
    ]
    # dp[k][x][y]：在 (x, y) 处、移动 k 次，棋子不出界的概率。
    dp = [
        [[-1 for _ in range(n)] for _ in range(n)] for _ in range(k+1)
    ]
    # 初始化
    for p in range(n):
        for q in range(n):
            dp[0][p][q] = 1.0

    def main_step(times: int, x: int, y: int) -> float:
        if dp[times][x][y] > -1:
            return dp[times][x][y]
        ans = 0
        for choice in directions:
            i = x + choice[0]
            j = y + choice[1]
            if 0 <= i < n and 0 <= j < n:
                ans += (1/8)*main_step(times-1, i, j)
        dp[times][x][y] = ans
        return ans

    return main_step(k, row, column)


print(knight_probability(3, 2, 0, 0))
print(knight_probability(1, 0, 0, 0))
print(knight_probability(8, 30, 6, 4))
