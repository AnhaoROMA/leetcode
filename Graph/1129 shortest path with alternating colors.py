"""
https://leetcode.com/problems/shortest-path-with-alternating-colors/

You are given an integer n,
the number of nodes in a directed graph where the nodes are labeled from 0 to n-1.
Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:
    redEdges[i] = [ai, bi] indicates that
        there is a directed red edge from node ai to node bi in the graph, and
    blueEdges[j] = [uj, vj] indicates that
        there is a directed blue edge from node uj to node vj in the graph.

Return an array answer of length n,
where each answer[x] is the length of the shortest path from node 0 to node x
such that the edge colors alternate along the path,
or -1 if such a path does not exist.
"""


def shortestAlternatingPaths(n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
    ans = [-1 for _ in range(n)]
    red = dict()
    for f, t in redEdges:
        if f not in red:
            red[f] = set()
        red[f].add(t)
    blue = dict()
    for f, t in blueEdges:
        if f not in blue:
            blue[f] = set()
        blue[f].add(t)
    # print(red)
    # print(blue)

    # 因为题目说了可能有自回路和平行线，所以要加上防止重复的机制。
    visited_from_red = set()
    visited_from_blue = set()

    bfs = list()
    ans[0] = 0
    if 0 in red:
        for y in red[0]:
            bfs.append((y, "R"))
            visited_from_red.add(y)
    if 0 in blue:
        for y in blue[0]:
            bfs.append((y, "B"))
            visited_from_blue.add(y)
    # print(bfs)

    count = 1
    while bfs:
        size = len(bfs)
        for _ in range(size):
            x, last_color = bfs.pop(0)
            if ans[x] < 0:
                ans[x] = count
            if last_color == "R":
                if x in blue:
                    for y in blue[x]:
                        if y in visited_from_blue:
                            continue
                        bfs.append((y, "B"))
                        visited_from_blue.add(y)
            else:
                if x in red:
                    for y in red[x]:
                        if y in visited_from_red:
                            continue
                        bfs.append((y, "R"))
                        visited_from_red.add(y)
        count += 1

    return ans


print(
    shortestAlternatingPaths(
        n=3,
        redEdges=[[0, 1], [1, 2]],
        blueEdges=[[1, 1]]
    )
)
