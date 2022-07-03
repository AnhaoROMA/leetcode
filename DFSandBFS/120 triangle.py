"""
https://leetcode.com/problems/triangle/

Given a triangle array, return the minimum path sum from top to bottom.

For each step,
you may move to an adjacent number of the row below. More formally,
if you are on index i on the current row,
you may move to either index i or index i + 1 on the next row.

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11.

Input: triangle = [[-10]]
Output: -10

Constraints:
    1 <= triangle.length <= 200
    triangle[0].length == 1
    triangle[i].length == triangle[i - 1].length + 1
    -10^4 <= triangle[i][j] <= 10^4
"""


def dfs(input: list[list[int]]) -> int:
    depth = len(input)
    result = 200 * 10 ** 4
    bfs = list()
    bfs.append(
        [0, input[0][0], 0]
    )
    while bfs:
        temp_depth, temp_value, temp_index = bfs.pop(0)
        if temp_depth == depth - 1:
            result = min(result, temp_value)
        else:
            left = temp_index
            right = temp_index + 1
            bfs.append(
                [temp_depth+1, temp_value+input[temp_depth+1][left], left]
            )
            bfs.append(
                [temp_depth+1, temp_value+input[temp_depth+1][right], right]
            )
    return result


def bottom_to_top(input: list[list[int]]) -> int:
    # 2
    # 3 4
    # 6 5 7
    # 4 1 8 3
    length = len(input)
    memory = [[0 for _ in range(length)] for _ in range(length)]
    # 最后一行
    cur_depth = length - 1
    for i in range(cur_depth+1):
        memory[cur_depth][i] = input[cur_depth][i]
    # 其他行
    cur_depth -= 1
    while cur_depth >= 0:
        for i in range(cur_depth+1):
            memory[cur_depth][i] = input[cur_depth][i] + \
                                   min(memory[cur_depth+1][i], memory[cur_depth+1][i+1])
        cur_depth -= 1
    return memory[0][0]


a = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(bottom_to_top(a))
