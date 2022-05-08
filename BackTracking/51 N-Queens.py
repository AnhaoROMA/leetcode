"""
https://leetcode.com/problems/n-queens/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement,
where 'Q' and '.' both indicate a queen and an empty space, respectively.

Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Input: n = 1
Output: [["Q"]]
"""


def whether_valid(board: list[str]) -> bool:
    location = list()
    for i in range(len(board)):
        if "Q" in board[i]:
            j = board[i].index("Q")
            location.append([i, j])
    # print(location)
    for i in range(len(location)):
        i_x = location[i][0]
        i_y = location[i][1]
        for j in range(i+1, len(location)):
            j_x = location[j][0]
            j_y = location[j][1]
            if i_x == j_x or i_y == j_y or abs(i_x - j_x) == abs(i_y - j_y):
                return False
    return True


def backtracking(board: list[str], row: int) -> bool:
    if row == len(board):
        print(board)
        return True
    for j in range(len(board)):
        tmp = board[row]
        tmp = tmp[:j] + "Q" + tmp[j+1:]
        board[row] = tmp
        if whether_valid(board) and backtracking(board, row+1):
            return True
        else:
            tmp = board[row]
            tmp = tmp[:j] + "." + tmp[j + 1:]
            board[row] = tmp
    return False


def queens(n: int) -> list[list[str]]:
    field = list()
    for _ in range(n):
        tmp = ""
        for _ in range(n):
            tmp += "."
        field.append(tmp)
    # print(field)
    backtracking(field, 0)
    return list()


# b = [".Q..", ".Q..", "Q...", "..Q."]
# print(whether_valid(b))
queens(4)
