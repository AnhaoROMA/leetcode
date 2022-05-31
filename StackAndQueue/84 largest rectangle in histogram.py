"""
https://leetcode.com/problems/largest-rectangle-in-histogram/

Given an array of integers heights
representing the histogram's bar height where the width of each bar is 1,
return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10

Input: heights = [2,4]
Output: 4
"""


# 解法参考：https://www.bilibili.com/video/BV1fi4y1d7YX?share_source=copy_web
def solution(heights: list[int]) -> int:
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


a = [2, 1, 5, 6, 2, 3]
print(solution(a))
