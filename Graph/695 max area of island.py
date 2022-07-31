"""
https://leetcode.com/problems/max-area-of-island/

You are given an m x n binary matrix grid.
An island is a group of 1's (representing land)
    connected 4-directionally (horizontal or vertical.)
You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid.
If there is no island, return 0.
"""


def max_area(grid: list[list[int]]) -> int:
    ans = 0

    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                temp_ans = 0
                dfs = [
                    (i, j)
                ]
                while dfs:
                    x, y = dfs.pop()
                    grid[x][y] = 0
                    temp_ans += 1
                    # (x-1, y)
                    if x > 0 and grid[x-1][y] == 1 and (x-1, y) not in dfs:
                        dfs.append(
                            (x-1, y)
                        )
                    # (x+1, y)
                    if x < m-1 and grid[x+1][y] == 1 and (x+1, y) not in dfs:
                        dfs.append(
                            (x+1, y)
                        )
                    # (x, y-1)
                    if y > 0 and grid[x][y-1] == 1 and (x, y-1) not in dfs:
                        dfs.append(
                            (x, y-1)
                        )
                    # (x, y+1)
                    if y < n-1 and grid[x][y+1] == 1 and (x, y+1) not in dfs:
                        dfs.append(
                            (x, y+1)
                        )
                ans = max(ans, temp_ans)
    return ans


print(
    max_area(
        [
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        ]
    )
)
print(
    max_area(
        [
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
    )
)
print(
    max_area(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 1, 1],
            [0, 0, 0, 1, 1]
        ]
    )
)
