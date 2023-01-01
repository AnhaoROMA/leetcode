"""
https://leetcode.com/problems/unique-paths-iii/
"""


def unique_paths(grid: list[list[int]]) -> int:
    m = len(grid)
    n = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def if_possible(pos, obstacles, dst) -> int:
        ans = 0
        for dx, dy in directions:
            x = pos[0] + dx
            y = pos[1] + dy
            if x < 0 or x > m-1 or y < 0 or y > n-1:
                continue
            if (x, y) in obstacles:
                continue
            if (x, y) == dst:
                if len(obstacles) == m * n - 1:
                    return 1
                else:
                    continue
            ans += if_possible((x, y), obstacles|{(x, y)}, dst)

        return ans

    where_to_start = (-1, -1)
    where_to_stop = (-1, -1)
    where_is_obstacle = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                where_to_start = (i, j)
            elif grid[i][j] == 2:
                where_to_stop = (i, j)
            elif grid[i][j] == -1:
                where_is_obstacle.add((i, j))
            else:
                pass
    where_is_obstacle.add(where_to_start)
    # print(where_to_start)
    # print(where_to_stop)
    # print(where_is_obstacle)

    return if_possible(pos=where_to_start, obstacles=where_is_obstacle, dst=where_to_stop)


print(
    unique_paths(
        [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, -1]
        ]
    )
)
print(
    unique_paths(
        [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 2]
        ]
    )
)
print(
    unique_paths(
        [
            [0, 1],
            [2, 0]
        ]
    )
)
