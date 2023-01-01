"""
https://leetcode.com/problems/find-if-path-exists-in-graph/

https://zhuanlan.zhihu.com/p/93647900
"""


def valid_path(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    """
    并查集
    """
    union_find = {
        i: i for i in range(n)
    }

    def find_ancestor(x: int) -> int:
        if union_find[x] == x:
            return x
        else:
            return find_ancestor(union_find[x])

    for edge in edges:
        union_find[find_ancestor(edge[0])] = find_ancestor(edge[1])

    return find_ancestor(source) == find_ancestor(destination)


# print(
#     valid_path(
#         n=3,
#         edges=[
#             [0, 1], [1, 2], [2, 0]
#         ],
#         source=0,
#         destination=2
#     )
# )
# print(
#     valid_path(
#         n=6,
#         edges=[
#             [0, 1],
#             [0, 2],
#             [3, 5],
#             [5, 4],
#             [4, 3]
#         ],
#         source=0,
#         destination=5
#     )
# )
# print(
#     valid_path(
#         n=10,
#         edges=[[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]],
#         source=5,
#         destination=9
#     )
# )
print(
    valid_path(
        n=10,
        edges=[[2, 6], [4, 7], [1, 2], [3, 5], [7, 9], [6, 4], [9, 8], [0, 1], [3, 0]],
        source=5,
        destination=9
    )
)
