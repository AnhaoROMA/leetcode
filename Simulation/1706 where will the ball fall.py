"""
https://leetcode.com/problems/where-will-the-ball-fall/
"""


def findBall(grid: list[list[int]]) -> list[int]:
    """
    仿真：落球问题

    我的想法是：不要考虑球体运动，把墙壁抽象成镜子、把球抽象成光线。
    （在本题中，墙壁/镜子都是45度角，在这种情况下，光线的运动轨迹要么是垂直，要么是水平。）

    当然这是一个“阉割版”的抽象：我们不允许出现向上反射的情况！
    """
    m = len(grid)
    n = len(grid[0])

    def where_to_fall(pos: int) -> int:
        # 初始化
        direction = "down"  # 指 “ 去向 ”
        i = 0
        j = pos
        # 开始仿真
        while i < m:
            # 要考虑碰壁（指左右两壁）的情况
            if j < 0 or j > n-1:
                return -1
            if grid[i][j] > 0:
                # 镜子 \
                if direction == "left":
                    # \ <-
                    # 如果是光线的话，光线会向上反射，但是我们这里用的是“阉割版”的抽象。
                    return -1
                elif direction == "down":
                    direction = "right"
                    i = i
                    j = j + 1
                else:
                    # direction == "right"
                    # -> \
                    direction = "down"
                    i = i + 1
                    j = j
            else:
                # 镜子 /
                if direction == "right":
                    return -1
                elif direction == "down":
                    direction = "left"
                    i = i
                    j = j - 1
                else:
                    # direction == "left"
                    direction = "down"
                    i = i + 1
                    j = j
        return j

    ans = [-1 for _ in range(n)]
    for x in range(n):
        ans[x] = where_to_fall(x)
    return ans


print(findBall([[-1]]))
print(
    findBall(
        [
            [1, 1, 1, -1,-1],
            [1, 1, 1, -1,-1],
            [-1,-1,-1, 1, 1],
            [1, 1, 1, 1, -1],
            [-1,-1,-1,-1,-1]
        ]
    )
)
print(
    findBall(
        [
            [ 1, 1, 1, 1, 1, 1],
            [-1,-1,-1,-1,-1,-1],
            [ 1, 1, 1, 1, 1, 1],
            [-1,-1,-1,-1,-1,-1]
        ]
    )
)
