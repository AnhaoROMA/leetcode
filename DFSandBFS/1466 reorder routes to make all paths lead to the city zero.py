"""
https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
"""


def minReorder(n: int, connections: list[list[int]]) -> int:
    graph_from_to = [set() for _ in range(n)]
    graph_to_from = [set() for _ in range(n)]
    for f, t in connections:
        graph_from_to[f].add(t)
        graph_to_from[t].add(f)
    bfs = [(0, -1)]
    result = 0
    while bfs:
        size = len(bfs)
        for _ in range(size):
            x, parent = bfs.pop(0)
            snapshot_graph_x = set(graph_from_to[x])
            for y in snapshot_graph_x:
                if y == parent:
                    continue
                result += 1
                graph_from_to[x].remove(y)
                graph_from_to[y].add(x)
                graph_to_from[x].add(y)
                graph_to_from[y].remove(x)
            for y in graph_to_from[x]:
                bfs.append((y, x))
    return result


print(
    minReorder(
        6,
        [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    )
)
