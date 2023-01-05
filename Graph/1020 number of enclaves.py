"""
https://leetcode.com/problems/number-of-enclaves/

enclave: 插在别国领域中的领土，飞地。
"""


def num_enclaves(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])

    def dfs(x, y) -> bool:
        # 判断 (x,y) 是否属于某块飞地。
        if x < 0 or x > m-1 or y < 0 or y > n-1:
            return False
        if grid[x][y] in {0, 2}:
            return True
        grid[x][y] = 2
        judge_1 = dfs(x-1, y)
        judge_2 = dfs(x+1, y)
        judge_3 = dfs(x, y-1)
        judge_4 = dfs(x, y+1)
        return judge_1 and judge_2 and judge_3 and judge_4

    ans = list()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                if dfs(i, j) is True:
                    ans.append((i, j))
    # len(ans) 即为飞地的数量（并非各飞地的面积之和）。
    # print(ans)

    # 将所有的飞地标记为 “3” 。
    while ans:
        i, j = ans.pop()
        grid[i][j] = 3
        if 0 <= i-1 < m and grid[i-1][j] not in {0, 3}:
            ans.append((i-1, j))
        if 0 <= i+1 < m and grid[i+1][j] not in {0, 3}:
            ans.append((i+1, j))
        if 0 <= j-1 < n and grid[i][j-1] not in {0, 3}:
            ans.append((i, j-1))
        if 0 <= j+1 < n and grid[i][j+1] not in {0, 3}:
            ans.append((i, j+1))
    # print(grid)

    res = 0
    for line in grid:
        res += line.count(3)
    return res


# print(
#     num_enclaves(
#         [
#             [0, 0, 0, 0],
#             [1, 0, 1, 0],
#             [0, 1, 1, 0],
#             [0, 0, 0, 0]
#         ]
#     )
# )
# print(
#     num_enclaves(
#         [
#             [0, 1, 1, 0],
#             [0, 0, 1, 0],
#             [0, 0, 1, 0],
#             [0, 0, 0, 0]
#         ]
#     )
# )
print(
    num_enclaves(
        [
            [0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0],
            [1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0]
        ]
    )
)
