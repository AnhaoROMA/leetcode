"""
https://leetcode.com/problems/surrounded-regions/

Given an m x n matrix board containing 'X' and 'O',
capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""


def solve(board: list[list[str]]) -> None:
    """
    参考 1254. Number of Closed Islands 。
    """
    m = len(board)
    n = len(board[0])
    visited = set()
    ans = set()

    def is_a_island(x: int, y: int) -> bool:
        if x < 0 or x > m-1 or y < 0 or y > n-1:
            return False
        elif board[x][y] == "X":
            return True
        elif (x, y) in visited:
            return True
        else:
            visited.add((x, y))
            result = True
            result &= is_a_island(x-1, y)
            result &= is_a_island(x+1, y)
            result &= is_a_island(x, y-1)
            result &= is_a_island(x, y+1)
            return result

    for i in range(m):
        for j in range(n):
            if board[i][j] == "O" and (i, j) not in visited:
                if is_a_island(i, j) is True:
                    ans.add((i, j))
    # print(ans)
    for i, j in ans:
        dfs = [(i, j)]
        while dfs:
            temp_i, temp_j = dfs.pop()
            board[temp_i][temp_j] = "X"
            if temp_i > 0 and board[temp_i-1][temp_j] == "O":
                dfs.append((temp_i-1, temp_j))
            if temp_i < m-1 and board[temp_i+1][temp_j] == "O":
                dfs.append((temp_i+1, temp_j))
            if temp_j > 0 and board[temp_i][temp_j-1] == "O":
                dfs.append((temp_i, temp_j-1))
            if temp_j < n-1 and board[temp_i][temp_j+1] == "O":
                dfs.append((temp_i, temp_j+1))


a = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
solve(board=a)
print(a)
b = [
    ["O", "O", "O", "O", "X", "X"],
    ["O", "O", "O", "O", "O", "O"],
    ["O", "X", "O", "X", "O", "O"],
    ["O", "X", "O", "O", "X", "O"],
    ["O", "X", "O", "X", "O", "O"],
    ["O", "X", "O", "O", "O", "O"]
]
solve(board=b)
print(b)
