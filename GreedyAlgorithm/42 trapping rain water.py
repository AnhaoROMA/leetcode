"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
"""


def find_depth(nums, left, right):
    array = nums[left:right+1]
    if len(array) < 3:
        return array[0]
    array.sort()
    depth = array[-2]
    return depth


def trapping_rain_water(nums):
    result = 0
    length = len(nums)

    left = 0
    right = left + 1
    while right < length:
        if nums[right] >= nums[left]:
            depth = find_depth(nums, left, right)
            for k in range(left, right+1):
                result += max(depth-nums[k], 0)
            left = right
            right = left + 1
        else:
            right += 1

    while left < length - 1:
        depth = find_depth(nums, left, right)
        new_right = left
        for searcher in range(left, right):
            if nums[searcher] >= depth:
                new_right = searcher
        right = new_right
        for k in range(left, right):
            result += max(depth - nums[k], 0)
        left = max(left+1, right)
        right = length
    return result


height = [5, 4, 1, 2]
print(trapping_rain_water(height))
