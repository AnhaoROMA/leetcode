"""
https://leetcode.com/problems/move-zeroes/

Given an integer array nums,
move all zeroes to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

"""
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""

"""
Input: nums = [0]
Output: [0]
"""


def move_zeroes(nums: list[int]):
    # [7, 1, 0, 4, 0, 8, 9]
    #        i  j
    # initialize i as the index of the first zero value
    # initialize j as the index of the first non-zero value after i
    length = len(nums)
    for i in range(length):
        if nums[i] == 0:
            break
    if i + 1 == length:
        return nums
    for j in range(i+1, length):
        if nums[j] != 0:
            break
    # move non-zero value forwards continually
    while j < length:
        if nums[j] != 0:
            nums[i] = nums[j]
            i = i + 1
        j = j + 1
    # set the leftovers as zero
    while i < length:
        nums[i] = 0
        i = i + 1
    return nums


array = [0]
print(move_zeroes(array))
