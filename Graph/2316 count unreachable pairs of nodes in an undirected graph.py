"""
https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

You are given an integer n.
There is an undirected graph with n nodes, numbered from 0 to n-1.
You are given a 2D integer array edges where edges[i] = [a_i, b_i] denotes that
    there exists an undirected edge connecting nodes a_i and b_i.

Return the number of pairs of different nodes that are unreachable from each other.

Input:
    n = 3,
    edges = [[0,1],[0,2],[1,2]]
Output:
    0
Explanation:
    There are no pairs of nodes that are unreachable from each other.
    Therefore, we return 0.

Input:
    n = 7,
    edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output:
    14
Explanation:
    There are 14 pairs of nodes that are unreachable from each other:
    [[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
    Therefore, we return 14.

Constraints:
    1 <= n <= 10^5
    0 <= edges.length <= 2*10^5
    edges[i].length == 2
    0 <= a_i, b_i < n
    a_i != b_i
    There are no repeated edges.
"""

from collections import Counter


def count_pairs(n: int, edges: list[list[int]]) -> int:
    """
    显然可以用 并查集 解决。
    """

    parent = [i for i in range(n)]

    # **** **** **** **** **** **** **** **** #
    rank = [1 for _ in range(n)]
    # **** **** **** **** **** **** **** **** #

    def find_root(node: int) -> int:
        node_root = node
        while parent[node_root] != node_root:
            node_root = parent[node_root]
        return node_root

    def union(x: int, y: int):
        x_root = find_root(x)
        y_root = find_root(y)
        if x_root == y_root:
            pass
        else:
            # **** **** **** **** **** **** **** **** #
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            elif rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            else:
                parent[y_root] = x_root
                rank[x_root] += 1
            # **** **** **** **** **** **** **** **** #

    for i, j in edges:
        union(i, j)
    # print(parent)
    # print(rank)

    for i in range(n):
        parent[i] = find_root(i)
    res = Counter(parent)
    result = []
    for r in res:
        result.append(res[r])

    # **** **** **** **** **** **** **** **** #
    #
    # TLE 的方法
    #
    # length = len(result)
    # ans = 0
    # for i in range(length - 1):
    #     for j in range(i + 1, length):
    #         ans += result[i] * result[j]
    #
    ans = 0
    for i in range(len(result)):
        ans += result[i]*(n-result[i])
    ans = ans // 2
    # **** **** **** **** **** **** **** **** #

    return ans


print(
    count_pairs(
        n=7,
        edges=[[0,2],[0,5],[2,4],[1,6],[5,4]]
    )
)
print(
    count_pairs(
        n=7,
        edges=[[1,3],[1,4],[2,5],[2,6],[1,0],[0,2]]
    )
)
