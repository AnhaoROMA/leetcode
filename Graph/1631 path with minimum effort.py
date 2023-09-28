"""
https://leetcode.com/problems/path-with-minimum-effort/

You are a hiker preparing for an upcoming hike.
You are given heights, a 2D array of size rows x columns,
where heights[row][col] represents the height of cell (row, col).
You are situated in the top-left cell, (0, 0),
    and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed).
You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Input:
    heights = [[1,2,2],[3,8,2],[5,3,5]]
Output:
    2
Explanation:
    The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
    This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.

Input:
    heights = [[1,2,3],[3,8,4],[5,3,5]]
Output:
    1
Explanation:
    The route of [1,2,3,4,5] has a maximum absolute difference of 1 in consecutive cells,
    which is better than route [1,3,5,3,5].

Input:
    heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
Output:
    0
Explanation:
    This route does not require any effort.

Constraints:
    rows == heights.length
    columns == heights[i].length
    1 <= rows, columns <= 100
    1 <= heights[i][j] <= 10^6
"""

import heapq


def minimum_effort_path(heights: list[list[int]]) -> int:
    """
    Optimal Dijkstra

    What is Dijkstra's Algorithm?
        Dijkstra's Algorithm is a classic graph algorithm that
            finds the shortest path from a source node to all other nodes in a weighted graph.
        In this case, the graph is represented by a 2D grid of cells, where
            each cell is a node and the edges between them represent the effort to move from one cell to another.

    Mechanics of Dijkstra's Algorithm in "Path With Minimum Effort"
        1. Initialize Priority Queue:
            The algorithm starts in the top-left corner (the source).
            The priority queue is initialized to store the effort needed to reach each cell from the source.
            The effort for the source itself is zero.
        2. Distance Matrix:
            A 2D array keeps track of the minimum effort required to reach each cell.
            Initially, this is set to infinity for all cells except the source.
        3. Iterate and Update Distances:
            The algorithm pops the cell with the smallest effort from the priority queue and explores its neighbors.
            The effort required to reach a neighbor is updated if a smaller effort is found.
        4. Early Exit:
            The algorithm stops when it reaches the bottom-right corner, returning the effort required to get there.
    """

    m = len(heights)
    n = len(heights[0])
    directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
    inf = 10 ** 7

    distances = [[inf for _ in range(n)] for _ in range(m)]
    distances[0][0] = 0

    minHeap = [(0, 0, 0)]
    while minHeap:
        effort, x, y = heapq.heappop(minHeap)

        # early exit
        if x == m - 1 and y == n - 1:
            return effort

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                new_effort = max(effort, abs(heights[x][y] - heights[nx][ny]))
                if new_effort < distances[nx][ny]:
                    distances[nx][ny] = new_effort
                    heapq.heappush(minHeap, (new_effort, nx, ny))

    return -1


# print(minimum_effort_path([[1,2],[3,8]]))
print(minimum_effort_path([[1,2,2],[3,8,2],[5,3,5]]))
