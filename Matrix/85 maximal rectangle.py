"""
https://leetcode.com/problems/maximal-rectangle/

Given a rows x cols binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.

Input:
matrix = [
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]
Output:
6
"""


# solution:
# 84题的翻版
def solution_84(heights: list[int]) -> int:
    heights = [0] + heights + [0]
    result = 0
    monotonic_stack = list()
    for i in range(len(heights)):
        if not monotonic_stack or heights[monotonic_stack[-1]] <= heights[i]:
            monotonic_stack.append(i)
        else:
            while monotonic_stack and heights[monotonic_stack[-1]] > heights[i]:
                height = heights[monotonic_stack[-1]]
                monotonic_stack.pop()
                width = i - monotonic_stack[-1] - 1
                result = max(result, height*width)
            monotonic_stack.append(i)
    return result


def solution(matrix: list[list[str]]) -> int:
    m = len(matrix)
    n = len(matrix[0])

    result = 0
    for x in range(m):
        temp = list()
        for y in range(n):
            height = 0
            for i in range(x, -1, -1):
                if matrix[i][y] == "0":
                    break
                else:
                    height += 1
            temp.append(height)
        result = max(result, solution_84(temp))
    return result


a = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"]
]
b = [["1", "0"]]
print(solution(b))
