"""
https://leetcode.com/problems/number-of-operations-to-make-network-connected/
"""


def make_connected(n: int, connections: list[list[int]]) -> int:
    # 我的想法：
    # 找出并查集的数量（n1）、以及冗余路径的数量（n2），
    # 如果 n1 <= n2+1 ，则可以实现全连接。
    # 否则，不可能实现全连接。
    union_find = [i for i in range(n)]
    redundant_routes = 0

    def find(x: int) -> int:
        if union_find[x] == x:
            return x
        else:
            return find(union_find[x])

    def merge(i: int, j: int) -> None:
        union_find[find(i)] = find(j)

    for node_1, node_2 in connections:
        if find(node_1) == find(node_2):
            redundant_routes += 1
        else:
            merge(node_1, node_2)
    for i in range(n):
        union_find[i] = find(i)
    # print(union_find)
    # print(redundant_routes)
    num_unions = len(set(union_find))
    if num_unions > redundant_routes + 1:
        return -1
    else:
        return num_unions - 1


print(
    make_connected(
        4,
        [[0, 1], [0, 2], [1, 2]]
    )
)
print(
    make_connected(
        6,
        [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3]]
    )
)
print(
    make_connected(
        6,
        [[0, 1], [0, 2], [0, 3], [1, 2]]
    )
)
