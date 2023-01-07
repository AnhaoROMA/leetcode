"""
https://leetcode.com/problems/shortest-bridge/

You are given an nxn binary matrix grid where 1 represents land and 0 represents water.

An island is a 4-directionally connected group of 1's not connected to any other 1's.
There are exactly two islands in grid.

You may change 0's to 1's to connect the two islands to form one island.

Return the smallest number of 0's you must flip to connect the two islands.

Constraints:
    n == grid.length == grid[i].length
    2 <= n <= 100
    grid[i][j] is either 0 or 1.
    There are exactly two islands in grid.
"""


def shortest_bridge(grid: list[list[int]]) -> int:
    n = len(grid)
    island_1 = list()
    stop = False
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                dfs = [(i, j)]
                stop = True
                break
        if stop is True:
            break
    # print(dfs)
    while dfs:
        x, y = dfs.pop()
        island_1.append((x, y))
        if x > 0 and grid[x-1][y] == 1 and (x-1, y) not in island_1 and (x-1, y) not in dfs:
            dfs.append((x-1, y))
        if x < n-1 and grid[x+1][y] == 1 and (x+1, y) not in island_1 and (x+1, y) not in dfs:
            dfs.append((x+1, y))
        if y > 0 and grid[x][y-1] == 1 and (x, y-1) not in island_1 and (x, y-1) not in dfs:
            dfs.append((x, y-1))
        if y < n-1 and grid[x][y+1] == 1 and (x, y+1) not in island_1 and (x, y+1) not in dfs:
            dfs.append((x, y+1))
    # print(len(island_1))
    ans = 0
    visited = set(island_1)
    bfs = list(island_1)
    while bfs:
        size = len(bfs)
        for _ in range(size):
            x, y = bfs.pop(0)
            if x > 0 and (x-1, y) not in visited:
                if grid[x-1][y] == 1:
                    return ans
                bfs.append((x-1, y))
                visited.add((x-1, y))
            if x < n-1 and (x+1, y) not in visited:
                if grid[x+1][y] == 1:
                    return ans
                bfs.append((x+1, y))
                visited.add((x+1, y))
            if y > 0 and (x, y-1) not in visited:
                if grid[x][y-1] == 1:
                    return ans
                bfs.append((x, y-1))
                visited.add((x, y-1))
            if y < n-1 and (x, y+1) not in visited:
                if grid[x][y+1] == 1:
                    return ans
                bfs.append((x, y+1))
                visited.add((x, y+1))
        ans += 1
    return -1


print(
    shortest_bridge(
        [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]
        ]
    )
)
print(
    shortest_bridge(
        [
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 1]
        ]
    )
)
print(
    shortest_bridge(
        [
            [0, 1],
            [1, 0]
        ]
    )
)
