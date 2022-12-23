"""
https://leetcode.com/problems/possible-bipartition/
"""


def possible_bipartition(n: int, dislikes: list[list[int]]) -> bool:
    """
    与 785 题对照着看。
    """

    # 首先建立邻接矩阵。
    # （注意本题是从 1 开始计数）
    graph = [[] for _ in range(n+1)]
    for dislike in dislikes:
        graph[dislike[0]].append(dislike[1])
        graph[dislike[1]].append(dislike[0])
    # print(graph)

    # 染色法
    # 因为本题限制了二分图，那么我们可以用 1 和 -1 作染料（ 0 表示未染色，也就是那些“无所谓、都行”的人 ）。
    colors = [0 for _ in range(n+1)]

    # 开始对每一个人进行染色。
    for i in range(1, n+1):
        if not graph[i] or colors[i] != 0:
            continue
        colors[i] = 1
        bfs = list()
        bfs.append(i)
        while bfs:
            cur = bfs.pop(0)
            for e in graph[cur]:
                if colors[e] != 0:
                    if colors[cur] == colors[e]:
                        return False
                else:
                    colors[e] = -1 * colors[cur]
                    bfs.append(e)

    return True


print(
    possible_bipartition(
        n=50,
        dislikes=[[5,41],[29,44],[5,11],[18,46],[22,48],[2,32],[7,22],[23,41],[17,46],[1,17]]
    )
)
# print(
#     possible_bipartition(
#         n=4,
#         dislikes=[
#             [1, 2],
#             [1, 3],
#             [2, 4]
#         ]
#     )
# )
# print(
#     possible_bipartition(
#         n=3,
#         dislikes=[
#             [1, 2],
#             [1, 3],
#             [2, 3]
#         ]
#     )
# )
