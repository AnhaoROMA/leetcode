"""
https://leetcode.com/problems/course-schedule-ii/
"""


# 第 207 题的增强版，要求返回学习顺序。
def finish_order(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    order = []

    # in_degrees：每个节点的入度
    in_degrees = [0 for _ in range(num_courses)]
    # graph：哈希表，表示某个节点是哪些节点的前驱。
    graph = [[] for _ in range(num_courses)]
    for edge in prerequisites:
        latter, former = edge
        in_degrees[latter] += 1
        graph[former].append(latter)
    # print(in_degrees)
    # print(graph)
    stop = False
    while not stop:
        stop = True
        # cur_nodes：当前入度为 0 的节点们。
        cur_nodes = []
        for i in range(num_courses):
            if in_degrees[i] == 0:
                stop = False
                cur_nodes.append(i)
                order.append(i)
        # 我们想要移除那些入度为 0 的节点，这里用“将其入度赋为 -1”代替。
        for node in cur_nodes:
            in_degrees[node] = -1
            successors = graph[node]
            for successor in successors:
                in_degrees[successor] -= 1

    # 如果尚有入度大于 0 的节点（也就是有环），则证明有上不了的课。
    for in_degree in in_degrees:
        if in_degree > 0:
            return []
    return order


print(
    finish_order(
        6,
        [
            [1, 0],
            [2, 3],
            [2, 1],
            [4, 2],
        ]
    )
)
