"""
https://leetcode.com/problems/is-graph-bipartite/
"""


def is_bipartite(graph: list[list[int]]) -> bool:
    n = len(graph)
    colors = [0 for _ in range(n)]
    for i in range(n):
        if not graph[i] or colors[i] != 0:
            continue
        colors[i] = 1
        bfs = [i]
        while bfs:
            cur = bfs.pop(0)
            for e in graph[cur]:
                if colors[e] != 0:
                    if colors[e] == colors[cur]:
                        return False
                else:
                    colors[e] = -1 * colors[cur]
                    bfs.append(e)
    return True


print(
    is_bipartite(
        [
            [1, 2, 3],
            [0, 2],
            [0, 1, 3],
            [0, 2]
        ]
    )
)
