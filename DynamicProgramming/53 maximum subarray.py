"""
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Input: nums = [1]
Output: 1

Input: nums = [5,4,-1,7,8]
Output: 23
"""


def solution(nums: list[int]) -> int:
    length = len(nums)
    local_max = nums[0]
    final_max = nums[0]
    for i in range(1, length):
        local_max = max(nums[i], local_max + nums[i])
        final_max = max(local_max, final_max)
    return final_max


a = [5, 4, -1, 7, 8]
print(solution(a))
