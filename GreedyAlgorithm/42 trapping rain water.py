"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""


def trap(height: list[int]) -> int:
    """
    https://www.youtube.com/watch?v=ZI2z5pq0TqA
    """
    maxL = []
    tempMaxL = 0
    for h in height:
        maxL.append(tempMaxL)
        tempMaxL = max(h, tempMaxL)
    maxR = []
    tempMaxR = 0
    for h in reversed(height):
        maxR = [tempMaxR] + maxR
        tempMaxR = max(h, tempMaxR)
    boundary = [min(maxL[i], maxR[i]) for i in range(len(height))]
    return sum(
        [
            max(0, boundary[i]-height[i]) for i in range(len(height))
        ]
    )


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
