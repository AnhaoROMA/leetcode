"""
https://leetcode.com/problems/sum-of-distances-in-tree/

There is an undirected connected tree
    with n nodes labeled from 0 to n-1 and n-1 edges.

You are given the integer n and the array edges
    where edges[i] = [ai, bi] indicates that
    there is an edge between nodes ai and bi in the tree.

Return an array answer of length n
    where answer[i] is the sum of the distances
    between the ith node in the tree and all other nodes.

Constraints:
    1 <= n <= 3 * 10^4
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    The given input represents a valid tree.
"""


def solution(n: int, edges: list[list[int]]) -> list[int]:
    """
    distances[i][j]: 从 i 到 j 的距离。

    思路：每添加一条边，都需要更新表格。

    同时，根据题目的意思，不会出现环。

    然而，MLE: 64 / 73 test cases passed.

    错误原因：根据报错，是内存消耗超标，那么，可以考虑用邻接矩阵表示图。
    """
    distances = [[0 for _ in range(n)] for _ in range(n)]
    for edge in edges:
        p = edge[0]
        q = edge[1]
        # p_connections：目前，有哪些节点可以连接到 p 节点？
        # q_connections：目前，有哪些节点可以连接到 q 节点？
        p_connections = []
        q_connections = []
        for i in range(n):
            if distances[p][i] > 0:
                p_connections.append(i)
        for i in range(n):
            if distances[q][i] > 0:
                q_connections.append(i)
        # 开始更新
        for i in p_connections:
            distances[q][i] = distances[p][i] + 1
            distances[i][q] = distances[q][i]
        for i in q_connections:
            distances[p][i] = distances[q][i] + 1
            distances[i][p] = distances[p][i]
        for i in p_connections:
            for j in q_connections:
                distances[i][j] = 1 + distances[q][j] + distances[p][i]
                distances[j][i] = distances[i][j]
        distances[p][q] = 1
        distances[q][p] = 1
    ans = [sum(distances[i]) for i in range(n)]
    return ans


def main(n: int, edges: list[list[int]]) -> list[int]:
    """
    根据上一种方法，做出改变。

    distances[i] = {j: k} 表示节点 i 与 节点 j 的距离为 k

    但是，TLE了。
    """
    distances = [{i: 0} for i in range(n)]
    for edge in edges:
        p = edge[0]
        q = edge[1]
        # p_connections：目前，有哪些节点可以连接到 p 节点？
        # q_connections：目前，有哪些节点可以连接到 q 节点？
        p_connections = list(distances[p].keys())
        q_connections = list(distances[q].keys())
        # 开始更新
        for i in p_connections:
            for j in q_connections:
                distances[i][j] = 1 + distances[q][j] + distances[p][i]
                distances[j][i] = distances[i][j]
    ans = [sum(list(distances[i].values())) for i in range(n)]
    return ans


def good_idea(n: int, edges: list[list[int]]) -> list[int]:
    """
    一个名叫 segment tree 的做法。
    B站 BV1ME411o7r6
    """
    # result 是我们要返回的数组
    result = [0 for _ in range(n)]
    # connections 为邻接矩阵（稀疏的）
    connections = [[] for _ in range(n)]
    # count 是 subtree 的 size
    count = [0 for _ in range(n)]
    for edge in edges:
        connections[edge[0]].append(edge[1])
        connections[edge[1]].append(edge[0])
    # print(connections)

    def post_order(root: int, parent: int):
        """
        后序遍历。

        目的有 2 个，其一是更新 count[]（主要），其二是更新 result[]。
        """
        for next in connections[root]:
            if next == parent:
                continue
            post_order(next, root)
            result[root] += result[next] + count[next]
            count[root] += count[next]
        count[root] += 1

    def pre_order(root: int, parent: int):
        """
        前序遍历。

        目的是 fill result[] 。
        """
        for next in connections[root]:
            if next == parent:
                continue
            result[next] = result[root] - count[next] + (n - count[next])
            pre_order(next, root)

    post_order(0, -1)
    pre_order(0, -1)
    return result


# print(solution(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
# print(solution(1, []))
# print(solution(2, [[1, 0]]))
# print(solution(3, [[2, 0], [1, 0]]))
# print(solution(4, [[2, 0], [3, 1], [2, 1]]))
# print(solution(6, [[1, 2], [1, 4], [5, 0], [3, 0], [3, 4]]))
# print(main(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
# print(main(1, []))
# print(main(2, [[1, 0]]))
# print(main(3, [[2, 0], [1, 0]]))
# print(main(4, [[2, 0], [3, 1], [2, 1]]))
# print(main(6, [[1, 2], [1, 4], [5, 0], [3, 0], [3, 4]]))
print(good_idea(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]))
print(good_idea(1, []))
print(good_idea(2, [[1, 0]]))
print(good_idea(3, [[2, 0], [1, 0]]))
print(good_idea(4, [[2, 0], [3, 1], [2, 1]]))
print(good_idea(6, [[1, 2], [1, 4], [5, 0], [3, 0], [3, 4]]))
