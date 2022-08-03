"""
https://leetcode.com/problems/knight-probability-in-chessboard/
"""


def knight_probability(n: int, k: int, row: int, column: int) -> float:
    """
    递归（带记忆），运用概率论中的加法公式与乘法公式。
    """
    directions = [
        (-1, -2), (-2, -1), (-2, 1), (-1, 2),
        (1, -2), (2, -1), (2, 1), (1, 2)
    ]
    memory = [[-1 for _ in range(n)] for _ in range(n)]

    def main_part(left_times: int, x: int, y: int) -> float:
        if left_times == 0:
            return 1.0
        if memory[x][y] > -1:
            return memory[x][y]
        ans = 0
        for choice in directions:
            i = x + choice[0]
            j = y + choice[1]
            if 0 <= i < n and 0 <= j < n:
                ans += (1/8)*main_part(left_times-1, i, j)
        memory[x][y] = ans
        return ans

    return main_part(left_times=k, x=row, y=column)


# print(knight_probability(3, 2, 0, 0))
# print(knight_probability(1, 0, 0, 0))
print(knight_probability(8, 30, 6, 4))
