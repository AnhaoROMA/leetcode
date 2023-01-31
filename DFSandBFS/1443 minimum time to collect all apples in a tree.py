"""
https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/

Given an undirected tree consisting of n vertices numbered from 0 to n-1,
which has some apples in their vertices.
You spend 1 second to walk over one edge of the tree.
Return the minimum time in seconds you have to spend to collect all apples in the tree,
starting at vertex 0 and coming back to this vertex.

The edges of the undirected tree are given in the array edges,
where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.
Additionally, there is a boolean array hasApple,
where hasApple[i] = true means that vertex i has an apple;
otherwise, it does not have any apple.

Constraints:
    1 <= n <= 10^5
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai < bi <= n - 1
    fromi < toi
    hasApple.length == n
"""


def minTime(n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
    next_nodes = [set() for _ in range(n)]
    for edge in edges:
        next_nodes[edge[0]].add(edge[1])
        next_nodes[edge[1]].add(edge[0])
    # print(next_nodes)

    def dfs(node: int, parent: int) -> int:
        ans = 0
        for next_node in next_nodes[node]:
            if next_node == parent:
                continue
            used_for_dfs_next_node = dfs(next_node, node)
            if used_for_dfs_next_node > 0 or hasApple[next_node] is True:
                ans += 2
            ans += used_for_dfs_next_node
        return ans

    return dfs(node=0, parent=-1)


print(
    minTime(
        n=4,
        edges=[[0, 1], [0, 2], [1, 3]],
        hasApple=[False, False, False, True]
    )
)
print(
    minTime(
        n=4,
        edges=[[0, 2], [0, 3], [1, 2]],
        hasApple=[False, True, False, False]
    )
)
print(
    minTime(
        n=7,
        edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        hasApple=[False, False, True, False, True, True, False]
    )
)
print(
    minTime(
        n=7,
        edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        hasApple=[False, False, True, False, False, True, False]
    )
)
print(
    minTime(
        n=7,
        edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        hasApple=[False, False, False, False, False, False, False]
    )
)
