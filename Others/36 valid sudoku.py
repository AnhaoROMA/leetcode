"""
https://leetcode.com/problems/valid-sudoku/

Determine if a 9 x 9 Sudoku board is valid.
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""


def check_sub_board(sub_board) -> bool:
    record = {
        "1": False,
        "2": False,
        "3": False,
        "4": False,
        "5": False,
        "6": False,
        "7": False,
        "8": False,
        "9": False,
    }
    for i in sub_board:
        if i == ".":
            continue
        if record[i] is True:
            return False
        else:
            record[i] = True
    return True


def if_valid(board) -> bool:
    # check row
    for row in board:
        if check_sub_board(row) is False:
            return False
    # check col
    for i in range(9):
        col = list()
        for j in range(9):
            col.append(board[j][i])
        if check_sub_board(col) is False:
            return False
    # check sub board
    temp = [0, 1, 2]
    for m in temp:
        for n in temp:
            sub = list()
            for i in range(9):
                for j in range(9):
                    if i // 3 == m and j // 3 == n:
                        sub.append(board[i][j])
            if check_sub_board(sub) is False:
                return False
    return True


board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
board2 = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]
print(if_valid(board2))
