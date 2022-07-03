"""
https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b,
and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities
and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1
if the ith city and the jth city are directly connected,
and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
"""


def findCircleNum(isConnected: list[list[int]]) -> int:
    ans = 0
    visited = set()
    n = len(isConnected)
    for i in range(n):
        if i not in visited:
            ans += 1
            dfs = list()
            dfs.append(i)
            while dfs:
                tmp = dfs.pop()
                visited.add(tmp)
                for j in range(n):
                    if isConnected[tmp][j] and j not in visited:
                        dfs.append(j)
    return ans


print(
    findCircleNum(
        [
            [1, 0, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],
            [1, 0, 1, 1]
        ]
    )
)
