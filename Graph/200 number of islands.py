import queue

"""
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""

"""
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
"""

"""
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

# 解题思路：https://www.bilibili.com/video/BV1xa411A76q?p=21&share_source=copy_web


def dfs(grid) -> int:
    result = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            stack = list()
            if grid[i][j] == "1":
                result += 1
                stack.append((i, j))
                while len(stack) > 0:
                    temp = stack.pop()
                    if grid[temp[0]][temp[1]] == "0":
                        continue
                    if temp[0] > 0 and grid[temp[0]-1][temp[1]] == "1":
                        stack.append((temp[0]-1, temp[1]))
                    if temp[0] < m-1 and grid[temp[0]+1][temp[1]] == "1":
                        stack.append((temp[0]+1, temp[1]))
                    if temp[1] > 0 and grid[temp[0]][temp[1]-1] == "1":
                        stack.append((temp[0], temp[1]-1))
                    if temp[1] < n-1 and grid[temp[0]][temp[1]+1] == "1":
                        stack.append((temp[0], temp[1]+1))

                    grid[temp[0]][temp[1]] = "0"
    return result


def bfs(grid) -> int:
    result = 0
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                q = queue.Queue()
                result += 1
                q.put((i, j))
                while q.empty() is False:
                    temp = q.get()
                    if grid[temp[0]][temp[1]] == "0":
                        continue
                    if temp[0] > 0 and grid[temp[0] - 1][temp[1]] == "1":
                        q.put((temp[0] - 1, temp[1]))
                    if temp[0] < m - 1 and grid[temp[0] + 1][temp[1]] == "1":
                        q.put((temp[0] + 1, temp[1]))
                    if temp[1] > 0 and grid[temp[0]][temp[1] - 1] == "1":
                        q.put((temp[0], temp[1] - 1))
                    if temp[1] < n - 1 and grid[temp[0]][temp[1] + 1] == "1":
                        q.put((temp[0], temp[1] + 1))

                    grid[temp[0]][temp[1]] = "0"
    return result


map = [
    ["1","1","1"],
    ["0","1","0"],
    ["1","1","1"]
]
print(dfs(map))
