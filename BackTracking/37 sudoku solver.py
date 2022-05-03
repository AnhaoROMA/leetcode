def whether_valid(board: list[list[str]]) -> bool:
    # have passed
    set_row = {
        "1": list(),
        "2": list(),
        "3": list(),
        "4": list(),
        "5": list(),
        "6": list(),
        "7": list(),
        "8": list(),
        "9": list()
    }
    set_col = {
        "1": list(),
        "2": list(),
        "3": list(),
        "4": list(),
        "5": list(),
        "6": list(),
        "7": list(),
        "8": list(),
        "9": list()
    }
    set_sub = {
        "1": list(),
        "2": list(),
        "3": list(),
        "4": list(),
        "5": list(),
        "6": list(),
        "7": list(),
        "8": list(),
        "9": list()
    }
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == ".":
                continue
            else:
                if i in set_row[val]:
                    return False
                else:
                    set_row[val].append(i)
                if j in set_col[val]:
                    return False
                else:
                    set_col[val].append(j)
                sub = (i // 3) * 3 + j // 3
                if sub in set_sub[val]:
                    return False
                else:
                    set_sub[val].append(sub)

    return True


def solve_sudoku(board: list[list[str]], x: int, y: int) -> bool:
    if x == 9:
        return True
    if y == 9:
        return solve_sudoku(board, x+1, 0)

    if board[x][y] != ".":
        return solve_sudoku(board, x, y+1)
    else:
        # board[x][y] == "."
        count = 1
        while count <= 9:
            board[x][y] = str(count)
            if whether_valid(board) and solve_sudoku(board, x, y+1):
                return True
            else:
                board[x][y] = "."
            count += 1
        return False
    return True


def solution(board: list[list[str]]):
    solve_sudoku(board, 0, 0)


a = [
    [".",".","9","7","4","8",".",".","."],
    ["7",".",".",".",".",".",".",".","."],
    [".","2",".","1",".","9",".",".","."],
    [".",".","7",".",".",".","2","4","."],
    [".","6","4",".","1",".","5","9","."],
    [".","9","8",".",".",".","3",".","."],
    [".",".",".","8",".","3",".","2","."],
    [".",".",".",".",".",".",".",".","6"],
    [".",".",".","2","7","5","9",".","."]
]
solution(board=a)
print(whether_valid(a))
