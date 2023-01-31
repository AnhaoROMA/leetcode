"""
https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
"""


def count(n: int, edges: list[list[int]], labels: str) -> list[int]:
    graph = [set() for _ in range(n)]
    for edge in edges:
        graph[edge[0]].add(edge[1])
        graph[edge[1]].add(edge[0])
    # print(graph)
    ans = [0 for _ in range(n)]

    def dfs(node: int, parent: int):
        summary = {
            "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0,
            "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0,
            "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
            "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0
        }
        summary[labels[node]] += 1
        for next_node in graph[node]:
            if next_node == parent:
                continue
            next_summary = dfs(next_node, node)
            for character in next_summary:
                summary[character] += next_summary[character]
        ans[node] = summary[labels[node]]
        return summary

    dfs(node=0, parent=-1)

    return ans


print(
    count(
        7,
        [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
        "abaedcd"
    )
)
print(
    count(
        4,
        [[0, 1], [1, 2], [0, 3]],
        "bbbb"
    )
)
print(
    count(
        5,
        [[0, 1], [0, 2], [1, 3], [0, 4]],
        "aabab"
    )
)
