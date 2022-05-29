"""
https://leetcode.com/problems/escape-the-spreading-fire/

Return the maximum number of minutes that you can stay in your initial position before moving
while still safely reaching the safehouse.
If this is impossible, return -1.
If you can always reach the safehouse regardless of the minutes stayed, return 109.

Note that even if the fire spreads to the safehouse immediately after you have reached it,
it will be counted as safely reaching the safehouse.
"""
MAX_VALUE = 10 ** 9


# solution 1 （我的解法，TLE了，但是是正确的）:
# 先找到所有可能的逃亡路径（刚开始）。
# 然后根据火势蔓延的时间，依次计算每条路径的最大延迟。
# 找出最大的延迟。
#
# 注意：在淘汰路径时，要考虑 火势蔓延到此路径的时间 与 人跑到该点的时间 ！
#
def find_route(graph: list[list[int]]) -> list:
    m = len(graph)
    n = len(graph[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    result = list()
    dfs = [
        [(0, 0)]
    ]
    while len(dfs) > 0:
        temp = dfs.pop()
        last = temp[-1]
        if last[0] == m-1 and last[1] == n-1:
            result.append(temp)
            continue
        for opt in directions:
            x = last[0] + opt[0]
            y = last[1] + opt[1]
            if x < 0 or x >= m or y < 0 or y >= n or graph[x][y] != 0 or ((x, y) in temp):
                continue
            else:
                dfs.append(temp + [(x, y)])
    return result


def solution(graph: list[list[int]]) -> int:
    m = len(graph)
    n = len(graph[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    all_possible_routes = find_route(graph)
    num_routes = len(all_possible_routes)
    if num_routes == 0:
        return -1
    result = [MAX_VALUE for _ in range(num_routes)]
    filled = [False for _ in range(num_routes)]
    time_ticket = 0

    old_fire = list()
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                old_fire.append((i, j))

    while False in filled:
        new_fire = list()
        for fire in old_fire:
            for opt in directions:
                x = fire[0] + opt[0]
                y = fire[1] + opt[1]
                if x < 0 or x >= m or y < 0 or y >= n or graph[x][y] != 0 or (x, y) in new_fire:
                    continue
                else:
                    new_fire.append((x, y))
        old_fire = new_fire

        if len(new_fire) == 0:
            return MAX_VALUE

        for i in range(num_routes):
            if filled[i] is True:
                continue
            for j in range(len(all_possible_routes[i])):
                if all_possible_routes[i][j] in new_fire:
                    if j == len(all_possible_routes[i]) - 1:
                        result[i] = min(result[i], time_ticket - j + 1)
                        filled[i] = True
                        break
                    elif time_ticket - j < 0:
                        result[i] = -1
                        filled[i] = True
                        break
                    else:
                        result[i] = min(result[i], time_ticket - j)

        for fire in new_fire:
            graph[fire[0]][fire[1]] = 1

        time_ticket += 1
    return max(result)


# solution 2:
# BFS与二分法
def duplicate_a_graph(graph: list[list[int]]) -> list[list[int]]:
    m = len(graph)
    n = len(graph[0])

    result = list()
    for i in range(m):
        temp = list()
        for j in range(n):
            temp.append(graph[i][j])
        result.append(temp)
    return result


def check(map: list[list[int]], time: int) -> bool:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    graph = duplicate_a_graph(map)
    m = len(graph)
    n = len(graph[0])

    old_fire = list()
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                old_fire.append((i, j))

    # 看看过了time个单位时间后，火势情况
    while time > 0 and old_fire:
        time -= 1
        new_fire = list()
        for fire in old_fire:
            for opt in directions:
                x = fire[0] + opt[0]
                y = fire[1] + opt[1]
                if x < 0 or x >= m or y < 0 or y >= n or graph[x][y] != 0 or (x, y) in new_fire:
                    continue
                elif x == 0 and y == 0:
                    return False
                else:
                    new_fire.append(
                        (x, y)
                    )
        for fire in new_fire:
            graph[fire[0]][fire[1]] = 1
        old_fire = new_fire

    visited = {(0, 0)}
    trace = [
        (0, 0)
    ]
    while trace:
        # 人先走
        new_trace = list()
        while trace:
            pos = trace.pop()
            for opt in directions:
                x = opt[0] + pos[0]
                y = opt[1] + pos[1]
                if x < 0 or x >= m or y < 0 or y >= n or graph[x][y] != 0 or (x, y) in visited:
                    continue
                elif x == m - 1 and y == n - 1:
                    return True
                else:
                    new_trace.append(
                        (x, y)
                    )
                    visited.add(
                        (x, y)
                    )

        # 火焰蔓延
        new_fire = list()
        for fire in old_fire:
            for opt in directions:
                x = fire[0] + opt[0]
                y = fire[1] + opt[1]
                if x < 0 or x >= m or y < 0 or y >= n or graph[x][y] != 0 or (x, y) in new_fire:
                    continue
                else:
                    new_fire.append(
                        (x, y)
                    )

        # 淘汰不可行的路径
        for i in range(len(new_trace)-1, -1, -1):
            if new_trace[i] in new_fire:
                new_trace.pop(i)

        # 整理，准备进入下一次循环
        trace = new_trace
        for fire in new_fire:
            graph[fire[0]][fire[1]] = 1
        old_fire = new_fire
    return False


def main(graph: list[list[int]]) -> int:
    m = len(graph)
    n = len(graph[0])

    left = -1
    right = m * n

    while left < right:
        middle = int((left+right+1)/2)
        if check(graph, middle):
            left = middle
        else:
            right = middle - 1

    if left < m * n:
        return left
    else:
        return MAX_VALUE


a = [
    [0, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 1, 0],
    [0, 2, 0, 0, 1, 2, 0],
    [0, 0, 2, 2, 2, 0, 2],
    [0, 0, 0, 0, 0, 0, 0]
]
b = [
    [0, 0, 0, 0],
    [0, 1, 2, 0],
    [0, 2, 0, 0]
]
c = [
    [0, 0, 0],
    [2, 2, 0],
    [1, 2, 0]
]
d = [
    [0, 2, 0, 0, 1],
    [0, 2, 0, 2, 2],
    [0, 2, 0, 0, 0],
    [0, 0, 2, 2, 0],
    [0, 0, 0, 0, 0]
]
e = [
    [0, 1],
    [0, 2],
    [0, 0]
]

# print(find_route(a))
# print(solution(a))
# print(solution(b))
# print(solution(c))
# print(solution(d))
# print(solution(e))

print(main(a))
print(main(b))
print(main(c))
print(main(d))
print(main(e))
