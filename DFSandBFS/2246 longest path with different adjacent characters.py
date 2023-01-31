"""
https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
"""


def longest_path(parent: list[int], s: str) -> int:
    """
    比较容易想到 DFS 。

    提示：
    对于某个节点，若求其 longest_path （以其为起点的 longest_path ） ，与其子树的根节点的 longest_path 有什么关系？
    """

    # sub_trees[i] --> 节点 i 的子树。
    length = len(parent)
    sub_trees = dict()
    for i in range(1, length):
        if parent[i] not in sub_trees:
            sub_trees[parent[i]] = set()
        sub_trees[parent[i]].add(i)
    # print(sub_trees)

    # record[i] --> 节点 i 的 longest_path 。
    record = [0 for _ in range(length)]

    def dfs(node: int) -> list[int]:
        if node not in sub_trees:
            record[node] = 1
            return [1]
        ans = []
        for next_node in sub_trees[node]:
            ans_next_node = dfs(next_node)
            if s[next_node] == s[node]:
                continue
            if ans_next_node:
                ans.append(1+max(ans_next_node))
        ans.sort()
        ans = ans[-2:]
        # print(str(node) + " -> " + str(ans))
        if len(ans) == 0:
            # 若 ans[] 的长度为零，
            # 也就是说，该节点虽然有 next_node(s)，但是 next_node(s) 的值与 node 的值相同，
            # 这种情况与“没有子树”的情形相同！
            ans = [1]
        if len(ans) == 1:
            record[node] = sum(ans)
        else:
            record[node] = sum(ans) - 1
        return ans

    # 对根节点进行 DFS ，目的是填充 record[] 。
    dfs(node=0)

    # print(record)
    return max(record)


print(
    longest_path(
        [-1, 0],
        "mm"
    )
)
print(
    longest_path(
        parent=[-1, 0, 0, 1, 1, 2],
        s="abacbe"
    )
)
print(
    longest_path(
        parent=[-1, 0, 0, 0],
        s="aabc"
    )
)
print(
    longest_path(
        parent=[-1, 0, 0, 0, 0],
        s="aabcd"
    )
)
print(
    longest_path(
        parent=[-1],
        s="a"
    )
)
