"""
https://leetcode.com/problems/unique-paths-ii/
"""


def paths_dfs(graph: list[list[int]]) -> int:
    if graph[0][0] == 1 or graph[-1][-1] == 1:
        return 0
    m = len(graph)
    n = len(graph[0])
    directions = [(0, 1), (1, 0)]
    result = 0
    dfs = [
        [[(0, 0)], 0, 0]
    ]
    while len(dfs) > 0:
        visited, x, y = dfs.pop()
        if x == m-1 and y == n-1:
            result += 1
            continue
        for option in directions:
            i = x + option[0]
            j = y + option[1]
            if i >= m or i < 0 or j >= n or j < 0 or (i, j) in visited or graph[i][j] == 1:
                continue
            else:
                dfs.append([visited + [(i, j)], i, j])
    return result


def paths_dp(graph: list[list[int]]) -> int:
    if graph[0][0] == 1 or graph[-1][-1] == 1:
        return 0
    m = len(graph)
    n = len(graph[0])
    dp = [[0 for _ in range(n)] for _ in range(m)]
    dp[-1][-1] = 1
    i = m - 1
    while i >= 0:
        j = n - 1
        while j >= 0:
            if graph[i][j] == 1:
                pass
            else:
                if i == m - 1:
                    down = 0
                else:
                    down = dp[i+1][j]
                if j == n - 1:
                    right = 0
                else:
                    right = dp[i][j+1]
                dp[i][j] = dp[i][j] + down + right
            j -= 1
        i -= 1
    return dp[0][0]


a = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
b = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
]
print(paths_dp(b))
