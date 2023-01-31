"""
https://leetcode.com/problems/redundant-connection/description/
"""


def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    """
    用 并查集 判断哪些部分早就被连通了。

    For example,
    Given edges [[1, 2], [1, 3], [2, 3]],
          1
         / \
        2 - 3
    Initially, there are 3 disjoint sets: 1, 2, 3.
    Edge [1, 2] connects 1 to 2, i.e., 1 and 2 are within the same connected component.
    Edge [1, 3] connects 1 to 3, i.e., 1 and 3 are within the same connected component.
    Edge [2, 3] connects 2 to 3,
        but 2 and 3 have been within the same connected component already,
        so [2, 3] is redundant.
    """
    n = len(edges)
    union_find = {i: i for i in range(1, n+1)}

    def find(x: int) -> int:
        if union_find[x] == x:
            return union_find[x]
        else:
            return find(union_find[x])

    def merge(x: int, y: int):
        union_find[find(x)] = find(y)

    for i, j in edges:
        if find(i) == find(j):
            return [i, j]
        else:
            merge(i, j)

    return [-1, -1]


print(
    findRedundantConnection(
        [[1, 2], [1, 3], [2, 3]]
    )
)
print(
    findRedundantConnection(
        [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]
    )
)
