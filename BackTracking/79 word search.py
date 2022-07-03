"""
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word,
return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Input:
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
],
word = "ABCCED"
Output:
true
"""


# def word_search(board: list[list[int]], word: str) -> bool:
#     m = len(board)
#     n = len(board[0])
#     word_length = len(word)
#     directions = [
#         (1, 0),
#         (-1, 0),
#         (0, 1),
#         (0, -1)
#     ]
#
#     for i in range(m):
#         for j in range(n):
#             if board[i][j] != word[0]:
#                 continue
#             else:
#                 dfs = [
#                     [
#                         [(i, j)], (i, j), 1
#                     ]
#                 ]
#                 while dfs:
#                     visited, position, matched = dfs.pop()
#                     if matched == word_length:
#                         return True
#                     for opt in directions:
#                         x = position[0] + opt[0]
#                         y = position[1] + opt[1]
#                         if x < 0 or y < 0 or x >= m or y >= n or (x, y) in visited:
#                             continue
#                         if board[x][y] != word[matched]:
#                             continue
#                         else:
#                             dfs.append(
#                                 [
#                                     visited + [(x, y)], (x, y), matched + 1
#                                 ]
#                             )
#
#     return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(x, y, p):
            if p == l:
                return True
            for dirx, diry in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                curx, cury = x + dirx, y + diry
                if 0 <= curx < m and 0 <= cury < n and \
                        flag[curx][cury] and board[curx][cury] == word[p]:
                    flag[curx][cury] = False
                    if dfs(curx, cury, p + 1):
                        flag[curx][cury] = True
                        return True
                    flag[curx][cury] = True
            return False

        m, n = len(board), len(board[0])
        l = len(word)
        flag = [[True] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    flag[i][j] = False
                    if dfs(i, j, 1):
                        return True
                    flag[i][j] = True
        return False


a = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"]
]
print(word_search(a, "ABCCED"))
print(word_search(a, "ABCB"))
print(word_search(a, "SEE"))
b = [
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "A"],
    ["A", "A", "A", "A", "A", "B"],
    ["A", "A", "A", "A", "B", "A"]
]
print(word_search(b, "AAAAAAAAAAAAABB"))
c = [
    ["C", "A", "A"],
    ["A", "A", "A"],
    ["B", "C", "D"]
]
print(word_search(c, "AAB"))
