"""
https://leetcode.com/problems/n-queens-ii/

The n-queens puzzle is the problem of placing n queens on an n x n chessboard
such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.
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


def dfs(temp):
    origin_board = temp[0]
    row = temp[1]

    result = list()
    for j in range(len(origin_board)):

        board = list()
        for element in origin_board:
            board.append(element)

        tmp = board[row]
        tmp = tmp[:j] + "Q" + tmp[j+1:]
        board[row] = tmp
        if whether_valid(board):
            result.append([board, row+1])
        else:
            tmp = board[row]
            tmp = tmp[:j] + "." + tmp[j + 1:]
            board[row] = tmp
    return result


def queens(n: int) -> list[list[str]]:
    result = 0

    stack = list()
    for i in range(n):
        field = list()
        for j in range(n):
            tmp = ""
            if j == 0:
                tmp = "." * i + "Q" + "." * (n-i-1)
            else:
                for _ in range(n):
                    tmp += "."
            field.append(tmp)
        stack.append([field, 1])

    while len(stack) > 0:
        temp = stack.pop()
        if temp[1] == n:
            result += 1
        else:
            stack += dfs(temp)

    return result


print(queens(9))
