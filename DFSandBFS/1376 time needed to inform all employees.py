"""
https://leetcode.com/problems/time-needed-to-inform-all-employees/
"""


def numOfMinutes(n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
    time_get_informed = [-1 for _ in range(n)]
    time_get_informed[headID] = 0

    def dfs(x: int) -> int:
        if time_get_informed[x] >= 0:
            return time_get_informed[x]
        else:
            time_get_informed[x] = informTime[manager[x]] + dfs(manager[x])
            return time_get_informed[x]

    for i in range(n):
        if time_get_informed[i] >= 0:
            continue
        time_get_informed[i] = dfs(i)
    return max(time_get_informed)
