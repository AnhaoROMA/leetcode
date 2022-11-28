"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
"""


def remove_stones(stones: list[list[int]]) -> int:
    """
    并查集
    """
    total_points = len(stones)

    # 初始化并查集
    stones.sort()
    union = dict()
    for x, y in stones:
        if x in union:
            union[x].add(y)
        else:
            union[x] = set()
            union[x].add(y)
    new_union = []
    for x in union:
        new_union.append(union[x])
    union = new_union
    del new_union
    del x
    del y
    print(union)

    # 开始归并
    length = len(union)
    stop = False
    while not stop:
        stop = True
        for i in range(length):
            for j in range(length-1, i, -1):
                if union[i] & union[j]:
                    union[i] = union[i] | union[j]
                    union.pop(j)
                    length -= 1
                    stop = False

    return total_points - length


# print(
#     remove_stones(
#         [
#             [0, 0],
#             [0, 1],
#             [1, 0],
#             [1, 2],
#             [2, 1],
#             [2, 2]
#         ]
#     )
# )
# print(
#     remove_stones(
#         [
#             [0, 0],
#             [0, 2],
#             [1, 1],
#             [2, 0],
#             [2, 2]
#         ]
#     )
# )
print(
    remove_stones(
        [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1],
            [2, 1],
            [2, 2],
            [3, 2],
            [3, 3],
            [3, 4],
            [4, 3],
            [4, 4]
        ]
    )
)
