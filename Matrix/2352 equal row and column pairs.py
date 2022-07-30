"""
https://leetcode.com/problems/equal-row-and-column-pairs/

Given a 0-indexed nxn integer matrix grid,
return the number of pairs (Ri, Cj) such that row Ri and column Cj are equal.

A row and column pair is considered equal
if they contain the same elements in the same order (i.e. an equal array).

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]

Constraints:
    n == grid.length == grid[i].length
    1 <= n <= 200
    1 <= grid[i][j] <= 10^5
"""


def pairs(grid: list[list[int]]) -> int:
    result = 0
    n = len(grid)

    grid_transposed = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            grid_transposed[i][j] = grid[j][i]
    # print(grid_transposed)
    for i in range(n):
        for j in range(n):
            if grid[i] == grid_transposed[j]:
                result += 1

    return result


a = [
    [3, 2, 1],
    [1, 7, 6],
    [2, 7, 7]
]
print(pairs(a))
