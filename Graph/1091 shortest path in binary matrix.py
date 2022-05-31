"""
https://leetcode.com/problems/shortest-path-in-binary-matrix/
"""
# 本题在BFS的基础上，有两个需要注意的地方：
# 1、集合的检索效率远超数组的
# 2、减少不必要的遍历


def search(grid: list[list[int]]) -> int:
    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1
    length = len(grid)
    if length == 1:
        return 1
    visited = {(0, 0)}  # 记录访问过的元素
    bfs = list()
    bfs.append([0, 0, 1])
    while len(bfs) > 0:
        temp = bfs.pop(0)
        x = temp[0]
        y = temp[1]
        temp_result = temp[2]
        if x == length - 1 and y == length - 1:
            return temp_result
        if x == 0 and y == 0:
            # 位于左上角
            # 可行的方向：右、下、右下
            if (x, y + 1) not in visited and grid[x][y+1] == 0:
                visited.add((x, y + 1))
                bfs.append([x, y + 1, temp_result+1])
            if (x + 1, y) not in visited and grid[x+1][y] == 0:
                visited.add((x + 1, y))
                bfs.append([x + 1, y, temp_result+1])
            if (x + 1, y + 1) not in visited and grid[x+1][y+1] == 0:
                visited.add((x + 1, y + 1))
                bfs.append([x + 1, y + 1, temp_result+1])
        elif x == 0 and y == length - 1:
            # 位于右上角
            # 可行的方向：左、下、左下
            if (x, y - 1) not in visited and grid[x][y - 1] == 0:
                visited.add((x, y - 1))
                bfs.append([x, y - 1, temp_result+1])
            if (x + 1, y) not in visited and grid[x+1][y] == 0:
                visited.add((x + 1, y))
                bfs.append([x+1, y, temp_result+1])
            if (x + 1, y - 1) not in visited and grid[x+1][y-1] == 0:
                visited.add((x + 1, y - 1))
                bfs.append([x+1, y-1, temp_result+1])
        elif x == length - 1 and y == 0:
            # 位于左下角
            # 可行的方向：上、右、右上
            if (x, y - 1) not in visited and grid[x][y - 1] == 0:
                visited.add((x, y - 1))
                bfs.append([x, y - 1, temp_result+1])
            if (x, y + 1) not in visited and grid[x][y + 1] == 0:
                visited.add((x, y + 1))
                bfs.append([x, y+1, temp_result+1])
            if (x - 1, y + 1) not in visited and grid[x - 1][y + 1] == 0:
                visited.add((x-1, y + 1))
                bfs.append([x - 1, y + 1, temp_result+1])
        elif x == 0:
            # 位于最上一行
            # 可行的方向：右、左、下、左下、右下
            if (x, y + 1) not in visited and grid[x][y+1] == 0:
                visited.add((x, y + 1))
                bfs.append([x, y+1, temp_result+1])
            if (x, y - 1) not in visited and grid[x][y - 1] == 0:
                visited.add((x, y - 1))
                bfs.append([x, y - 1, temp_result+1])
            if (x + 1, y) not in visited and grid[x+1][y] == 0:
                visited.add((x+1, y))
                bfs.append([x+1, y, temp_result+1])
            if (x + 1, y - 1) not in visited and grid[x+1][y-1] == 0:
                visited.add((x+1, y - 1))
                bfs.append([x+1, y-1, temp_result+1])
            if (x + 1, y + 1) not in visited and grid[x+1][y+1] == 0:
                visited.add((x+1, y + 1))
                bfs.append([x+1, y+1, temp_result+1])
        elif x == length - 1:
            # 位于最下一行
            # 可行的方向：右、左、上、左上、右上
            if (x, y + 1) not in visited and grid[x][y + 1] == 0:
                visited.add((x, y + 1))
                bfs.append([x, y + 1, temp_result+1])
            if (x, y - 1) not in visited and grid[x][y - 1] == 0:
                visited.add((x, y - 1))
                bfs.append([x, y - 1, temp_result+1])
            if (x - 1, y) not in visited and grid[x - 1][y] == 0:
                visited.add((x-1, y))
                bfs.append([x - 1, y, temp_result+1])
            if (x - 1, y - 1) not in visited and grid[x - 1][y - 1] == 0:
                visited.add((x-1, y - 1))
                bfs.append([x - 1, y - 1, temp_result+1])
            if (x - 1, y + 1) not in visited and grid[x - 1][y + 1] == 0:
                visited.add((x-1, y + 1))
                bfs.append([x - 1, y + 1, temp_result+1])
        elif y == 0:
            # 位于最左一行
            # 可行的方向：上、下、右、右下、右上
            if (x - 1, y) not in visited and grid[x-1][y] == 0:
                visited.add((x-1, y))
                bfs.append([x-1, y, temp_result+1])
            if (x + 1, y) not in visited and grid[x + 1][y] == 0:
                visited.add((x+1, y))
                bfs.append([x + 1, y, temp_result+1])
            if (x, y + 1) not in visited and grid[x][y + 1] == 0:
                visited.add((x, y + 1))
                bfs.append([x, y + 1, temp_result+1])
            if (x - 1, y + 1) not in visited and grid[x - 1][y + 1] == 0:
                visited.add((x-1, y + 1))
                bfs.append([x - 1, y + 1, temp_result+1])
            if (x + 1, y + 1) not in visited and grid[x + 1][y + 1] == 0:
                visited.add((x+1, y + 1))
                bfs.append([x + 1, y + 1, temp_result+1])
        elif y == length - 1:
            # 位于最右一行
            # 可行的方向：上、下、左、左下、左上
            if (x - 1, y) not in visited and grid[x-1][y] == 0:
                visited.add((x-1, y))
                bfs.append([x-1, y, temp_result+1])
            if (x + 1, y) not in visited and grid[x + 1][y] == 0:
                visited.add((x+1, y))
                bfs.append([x + 1, y, temp_result+1])
            if (x, y - 1) not in visited and grid[x][y - 1] == 0:
                visited.add((x, y - 1))
                bfs.append([x, y - 1, temp_result+1])
            if (x - 1, y - 1) not in visited and grid[x - 1][y - 1] == 0:
                visited.add((x-1, y - 1))
                bfs.append([x - 1, y - 1, temp_result+1])
            if (x + 1, y - 1) not in visited and grid[x + 1][y - 1] == 0:
                visited.add((x+1, y - 1))
                bfs.append([x + 1, y - 1, temp_result+1])
        else:
            if (x - 1, y) not in visited and grid[x - 1][y] == 0:
                visited.add((x-1, y))
                bfs.append([x - 1, y,temp_result+1])
            if (x + 1, y) not in visited and grid[x + 1][y] == 0:
                visited.add((x+1, y))
                bfs.append([x + 1, y, temp_result+1])
            if (x, y + 1) not in visited and grid[x][y + 1] == 0:
                visited.add((x, y + 1))
                bfs.append([x, y + 1, temp_result+1])
            if (x, y - 1) not in visited and grid[x][y - 1] == 0:
                visited.add((x, y - 1))
                bfs.append([x, y - 1, temp_result+1])
            if (x - 1, y + 1) not in visited and grid[x - 1][y + 1] == 0:
                visited.add((x-1, y + 1))
                bfs.append([x - 1, y + 1, temp_result+1])
            if (x + 1, y + 1) not in visited and grid[x + 1][y + 1] == 0:
                visited.add((x+1, y + 1))
                bfs.append([x + 1, y + 1, temp_result+1])
            if (x + 1, y - 1) not in visited and grid[x + 1][y - 1] == 0:
                visited.add((x+1, y - 1))
                bfs.append([x + 1, y - 1, temp_result+1])
            if (x - 1, y - 1) not in visited and grid[x - 1][y - 1] == 0:
                visited.add((x-1, y - 1))
                bfs.append([x - 1, y - 1, temp_result+1])
    return -1


a = [
    [0, 1],
    [1, 0]
]
b = [
    [0, 0, 0],
    [1, 1, 0],
    [1, 1, 0]
]
c = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
d = [
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0]
]
print(search(d))
