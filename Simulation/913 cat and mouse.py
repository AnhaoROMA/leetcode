"""
https://leetcode.com/problems/cat-and-mouse/

《 51世界游戏大全》之《兔子和猎犬》！
"""


def hare_and_hound(graph: list[list[int]]) -> int:
    pass


#
# 4 -- 3 -- 1
# |    |
# 2 -- 5
# |  /
# |/
# 0
#
print(
    hare_and_hound(
        [
            [2, 5],
            [3],
            [0, 4, 5],
            [1, 4, 5],
            [2, 3],
            [0, 2, 3]
        ]
    )
)
# #
# # 0 -- 1
# # |
# # 3 -- 2
# #
# print(
#     hare_and_hound(
#         [
#             [1, 3],
#             [0],
#             [3],
#             [0, 2]
#         ]
#     )
# )
