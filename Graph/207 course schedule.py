"""
https://leetcode.com/problems/course-schedule/

There are a total of numCourses courses you have to take,
labeled from 0 to numCourses-1.
You are given an array prerequisites
    where prerequisites[i] = [ai, bi] indicates that
    you must take course bi first if you want to take course ai.
For example, the pair [0, 1],
indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses.
Otherwise, return false.
"""


# 方法一：拓扑排序（前驱图）
# 方法是每次选择入度为 0 的节点，然后移除该节点，且该节点能到达的所有节点的入度减一。
def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
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
        # 我们想要移除那些入度为 0 的节点，这里用“将其入度赋为 -1”代替。
        for node in cur_nodes:
            in_degrees[node] = -1
            successors = graph[node]
            for successor in successors:
                in_degrees[successor] -= 1
    # 如果尚有入度大于 0 的节点（也就是有环），则证明有上不了的课。
    for in_degree in in_degrees:
        if in_degree > 0:
            return False
    return True


print(
    can_finish(
        6,
        [
            [1, 0],
            [2, 3],
            [2, 1],
            [4, 2],
            [3, 4]
        ]
    )
)
