"""
https://leetcode.com/problems/perfect-rectangle/
"""


def perfect_rectangle(rectangles: list[list[int]]) -> bool:
    """
    思想：
    - 小矩形的面积之和 应当等于 最后的矩形的面积。
    - 有且仅有 4 个点出现过 1 次，其余的点的出现次数不是 2 就是 4 。
        (注意，后来我发现了这一条的错误，改为“仅 4 个顶点出现了 1 次”。)
    """
    global_top = -1*10**6
    global_bottom = 10**6
    global_left = 10**6
    global_right = -1*10**6

    sum_squares = 0
    points_record = dict()
    for rectangle in rectangles:
        # 计算小矩形的面积
        sum_squares += (rectangle[2]-rectangle[0])*(rectangle[3]-rectangle[1])
        # 重新划边界线
        global_top = max(global_top, rectangle[3])
        global_bottom = min(global_bottom, rectangle[1])
        global_left = min(global_left, rectangle[0])
        global_right = max(global_right, rectangle[2])
        # 计数
        if (rectangle[0], rectangle[1]) not in points_record:
            points_record[(rectangle[0], rectangle[1])] = 1
        else:
            points_record[(rectangle[0], rectangle[1])] += 1
        if (rectangle[0], rectangle[3]) not in points_record:
            points_record[(rectangle[0], rectangle[3])] = 1
        else:
            points_record[(rectangle[0], rectangle[3])] += 1
        if (rectangle[2], rectangle[3]) not in points_record:
            points_record[(rectangle[2], rectangle[3])] = 1
        else:
            points_record[(rectangle[2], rectangle[3])] += 1
        if (rectangle[2], rectangle[1]) not in points_record:
            points_record[(rectangle[2], rectangle[1])] = 1
        else:
            points_record[(rectangle[2], rectangle[1])] += 1

    global_square = (global_top-global_bottom)*(global_right-global_left)
    # print(global_square)
    # print(sum_squares)
    if global_square != sum_squares:
        return False
    # print(points_record)
    # print(global_top)
    # print(global_bottom)
    # print(global_left)
    # print(global_right)
    if (global_left, global_bottom) not in points_record:
        return False
    elif points_record[(global_left, global_bottom)] != 1:
        return False
    else:
        del points_record[(global_left, global_bottom)]
    if (global_right, global_bottom) not in points_record:
        return False
    elif points_record[(global_right, global_bottom)] != 1:
        return False
    else:
        del points_record[(global_right, global_bottom)]
    if (global_left, global_top) not in points_record:
        return False
    elif points_record[(global_left, global_top)] != 1:
        return False
    else:
        del points_record[(global_left, global_top)]
    if (global_right, global_top) not in points_record:
        return False
    elif points_record[(global_right, global_top)] != 1:
        return False
    else:
        del points_record[(global_right, global_top)]

    for point in points_record:
        if points_record[point] not in {2, 4}:
            print(point)
            return False
    return True


# print(
#     perfect_rectangle(
#         [
#             [1, 1, 3, 3],
#             [3, 1, 4, 2],
#             [3, 2, 4, 4],
#             [1, 3, 2, 4],
#             [2, 3, 3, 4]
#         ]
#     )
# )
# print(
#     perfect_rectangle(
#         [
#             [1, 1, 3, 3],
#             [3, 1, 4, 2],
#             [1, 3, 2, 4],
#             [2, 2, 4, 4]
#         ]
#     )
# )
# print(
#     perfect_rectangle(
#         [
#             [1, 1, 2, 3],
#             [1, 3, 2, 4],
#             [3, 1, 4, 2],
#             [3, 2, 4, 4]
#         ]
#     )
# )
# print(
#     perfect_rectangle(
#         [
#             [0, 0, 1, 1],
#             [0, 0, 2, 1],
#             [1, 0, 2, 1],
#             [0, 2, 2, 3]
#         ]
#     )
# )
print(
    perfect_rectangle(
        [
            [0, 0, 4, 1],
            [7, 0, 8, 2],
            [6, 2, 8, 3],
            [5, 1, 6, 3],
            [4, 0, 5, 1],
            [6, 0, 7, 2],
            [4, 2, 5, 3],
            [2, 1, 4, 3],
            [0, 1, 2, 2],
            [0, 2, 2, 3],
            [4, 1, 5, 2],
            [5, 0, 6, 1]
        ]
    )
)
