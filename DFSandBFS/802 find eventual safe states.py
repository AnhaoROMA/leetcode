"""
https://leetcode.com/problems/find-eventual-safe-states/
"""


def eventual_safe_nodes(graph: list[list[int]]) -> list[int]:
    n = len(graph)

    visited = set()
    ans = set()

    def whether(node: int) -> bool:
        if node in visited:
            if node in ans:
                return True
            else:
                return False
        visited.add(node)
        if not graph[node]:
            ans.add(node)
            return True
        else:
            temp = True
            for next_node in graph[node]:
                temp = temp and whether(next_node)
            if temp is True:
                ans.add(node)
            return temp

    for i in range(n):
        whether(i)

    ans = list(ans)
    ans.sort()
    return ans


print(
    eventual_safe_nodes(
        [[1, 2], [2, 3], [5], [0], [5], [], []]
    )
)
print(
    eventual_safe_nodes(
        [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
    )
)
