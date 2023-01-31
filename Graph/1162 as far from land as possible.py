"""
https://leetcode.com/problems/as-far-from-land-as-possible/
"""


def max_distance(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    bfs = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                bfs.append((i, j))
    ans = 0
    while bfs:
        size = len(bfs)
        for _ in range(size):
            x, y = bfs.pop(0)
            if x > 0 and grid[x-1][y] == 0:
                grid[x-1][y] = ans + 2
                bfs.append((x-1, y))
            if x < m-1 and grid[x+1][y] == 0:
                grid[x+1][y] = ans + 2
                bfs.append((x+1, y))
            if y > 0 and grid[x][y-1] == 0:
                grid[x][y-1] = ans + 2
                bfs.append((x, y-1))
            if y < n-1 and grid[x][y+1] == 0:
                grid[x][y+1] = ans + 2
                bfs.append((x, y+1))
        ans += 1
    if ans == 1:
        return -1
    else:
        return ans - 1


print(
    max_distance(
        [
            [1, 0, 1],
            [0, 0, 0],
            [1, 0, 1]
        ]
    )
)
print(
    max_distance(
        [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
    )
)
