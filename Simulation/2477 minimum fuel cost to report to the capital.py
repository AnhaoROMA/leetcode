"""
https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/
"""


def minimumFuelCost(roads: list[list[int]], seats: int) -> int:
    n = len(roads) + 1
    # graph[] -> 邻接图
    graph = {i: set() for i in range(n)}
    for road in roads:
        graph[road[0]].add(road[1])
        graph[road[1]].add(road[0])

    result = [-1 for _ in range(n)]

    def dfs(x: int, parent: int) -> int:
        ans = 1
        # ans 为 countTreeNodes(x, parent)。
        for y in graph[x]:
            if y == parent:
                continue
            ans += dfs(y, x)
        # 在 x 集合后，这些人（总计 ans 人）从 x 返回 parent 需要用到 (ans-1)//seats+1 辆车。
        result[x] = (ans-1)//seats+1
        return ans

    dfs(x=0, parent=-1)
    # print(result)
    return sum(result[1:])


print(
    minimumFuelCost(
        roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]],
        seats=2
    )
)
print(
    minimumFuelCost(
        roads=[[0, 1], [0, 2], [0, 3]],
        seats=5
    )
)
print(
    minimumFuelCost(
        roads=[],
        seats=1
    )
)
print(
    minimumFuelCost(
        roads=[[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6], [2, 7], [7, 8], [8, 9]],
        seats=2
    )
)
