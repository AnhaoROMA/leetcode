"""
https://leetcode.com/problems/min-cost-to-connect-all-points/

You are given an array points representing integer coordinates of some points on a 2D-plane,
where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them:
    |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected.
All points are connected if there is exactly one simple path between any two points.

Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18

Constraints:
    1 <= points.length <= 1000
    -10^6 <= xi, yi <= 10^6
    All pairs (xi, yi) are distinct.
"""


def min_cost_connect_points(points: list[list[int]]) -> int:
    """
    对 Prim / Kruskal 算法进行一丢丢调整。
    """

    def manhattan_distance(x1, y1, x2, y2) -> int:
        return abs(x1 - x2) + abs(y1 - y2)

    distances_info = []
    latest_x, latest_y = points.pop(0)
    for x, y in points:
        distances_info.append(
            [
                manhattan_distance(latest_x, latest_y, x, y),
                (x, y)
            ]
        )
    total_cost = 0
    while distances_info:
        distances_info.sort()
        cost, (latest_x, latest_y) = distances_info.pop(0)
        total_cost += cost
        for i in range(len(distances_info)):
            x, y = distances_info[i][1]
            distances_info[i][0] = min(manhattan_distance(latest_x, latest_y, x, y), distances_info[i][0])
    return total_cost


print(min_cost_connect_points([[0,0],[2,2],[3,10],[5,2],[7,0]]))
print(min_cost_connect_points([[3,12],[-2,5],[-4,1]]))
