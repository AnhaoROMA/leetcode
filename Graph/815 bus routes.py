"""
https://leetcode.com/problems/bus-routes/
"""


def bus_routes_1(routes: list[list[int]], source: int, target: int) -> int:
    """
    本题最难的部分其实是想到构图的方法。
    """

    if source == target:
        return 0

    # 构图：某一点的邻接结点满足 “ 乘坐 1 路即可到达 ”。
    graph = dict()
    for route in routes:
        for bus_station in route:
            if bus_station not in graph:
                graph[bus_station] = set()
            graph[bus_station] = graph[bus_station] | set(route)
    for bus_station in graph:
        graph[bus_station].remove(bus_station)
    # print(graph)

    # BFS
    visited = set()  # 防止重复运算
    bfs = [(source, 1)]
    visited.add(source)
    while bfs:
        temp_station, temp_count = bfs.pop(0)
        for next_station in graph[temp_station]:
            if next_station == target:
                return temp_count
            if next_station in visited:
                continue
            visited.add(next_station)
            bfs.append((next_station, temp_count+1))
    return -1


def bus_routes_2(routes: list[list[int]], source: int, target: int) -> int:
    """
    本题最难的部分其实是想到构图的方法。
    """

    if source == target:
        return 0

    station_routes = dict()  # 用于记录某一站点属于哪些线路。
    for route_num, route in enumerate(routes):
        for bus_station in route:
            if bus_station not in station_routes:
                station_routes[bus_station] = set()
            station_routes[bus_station].add(route_num)
    # print(station_routes)

    bfs = [(source, 1)]
    visited_routes = set()
    while bfs:
        cur_station, count = bfs.pop(0)
        for route_i in station_routes[cur_station]:
            if route_i in visited_routes:
                continue
            visited_routes.add(route_i)
            for next_station in routes[route_i]:
                if next_station == target:
                    return count
                bfs.append((next_station, count+1))
    return -1


print(
    bus_routes_2(
        [[1, 2, 7], [3, 6, 7]],
        1,
        6
    )
)
print(
    bus_routes_2(
        [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]],
        15,
        12
    )
)
