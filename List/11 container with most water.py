"""
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

# solution: 双指针
# 用两个指针从两端开始向中间靠拢，
# 如果左端线段短于或等于右端，那么左端右移，反之右端左移，直到左右两端移到中间重合，
# 记录这个过程中每一次组成木桶的容积，返回其中最大的。


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        i = 0
        j = len(height) - 1
        while abs(j - i) > 0:
            temp = min(height[i], height[j]) * (j - i)
            if temp > result:
                result = temp
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return result
