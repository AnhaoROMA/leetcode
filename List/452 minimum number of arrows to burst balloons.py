"""
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
"""


def find_min_shots(points: list[list[int]]) -> int:
    points.sort()
    length = len(points)
    result = 1
    # i = points[0][0]
    j = points[0][1]
    for k in range(1, length):
        if points[k][0] > j:
            result += 1
            # i = points[k][0]
            j = points[k][1]
        else:
            # i = points[k][0]
            j = min(j, points[k][1])
    return result


print(
    find_min_shots(
        [[10, 16], [2, 8], [1, 6], [7, 12]]
    )
)
print(
    find_min_shots(
        [[1, 2], [3, 4], [5, 6], [7, 8]]
    )
)
print(
    find_min_shots(
        [[1, 2], [2, 3], [3, 4], [4, 5]]
    )
)
