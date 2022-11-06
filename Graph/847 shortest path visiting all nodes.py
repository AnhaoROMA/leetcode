"""
https://leetcode.com/problems/shortest-path-visiting-all-nodes/
"""


def shortest_path_length(graph: list[list[int]]) -> int:
    """
    保存出现过的状态：seen[]
    """
    n = len(graph)
    seen = set()

    bfs = list()
    for i in range(n):
        tmp = "0" * n
        tmp = tmp[:i] + "1" + tmp[i+1:]
        bfs.append((i, tmp, 0))
        seen.add(str(i)+"+"+tmp)
    # print(bfs)

    while bfs:
        node, visited, count = bfs.pop(0)
        if "0" not in visited:
            return count
        for next_node in graph[node]:
            next_visited = visited[:next_node] + "1" + visited[next_node+1:]
            next_status = str(next_node) + "+" + next_visited
            if next_status not in seen:
                bfs.append((next_node, next_visited, count+1))
                seen.add(str(next_node)+"+"+next_visited)
    return -1


print(
    shortest_path_length(
        [
            [1, 2, 3],
            [0],
            [0],
            [0]
        ]
    )
)
print(
    shortest_path_length(
        [
            [1],
            [0, 2, 4],
            [1, 3, 4],
            [2],
            [1, 2]
        ]
    )
)
print(
    shortest_path_length(
        [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 2, 3, 4, 5, 6, 7, 8, 9],
            [0, 1, 3, 4, 5, 6, 7, 8, 9],
            [0, 1, 2, 4, 5, 6, 7, 8, 9],
            [0, 1, 2, 3, 5, 6, 7, 8, 9],
            [0, 1, 2, 3, 4, 6, 7, 8, 9],
            [0, 1, 2, 3, 4, 5, 7, 8, 9],
            [0, 1, 2, 3, 4, 5, 6, 8, 9],
            [0, 1, 2, 3, 4, 5, 6, 7, 9, 10],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 11],
            [8],
            [9]
        ]
    )
)
