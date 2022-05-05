"""
https://leetcode.com/problems/permutations-ii/

Given a collection of numbers, nums, that might contain duplicates,
return all possible unique permutations in any order.
"""

"""
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
"""


def permute2(nums: list[int]) -> list[list[int]]:
    result = list()
    visited = list()
    length = len(nums)
    if length == 1:
        result.append([nums[0]])
    elif length == 2:
        result.append([nums[0], nums[1]])
        if nums[0] != nums[1]:
            result.append([nums[1], nums[0]])
    else:
        for i in range(length):
            if nums[i] in visited:
                continue
            visited.append(nums[i])
            left = nums[:i] + nums[i+1:]
            left_result = permute2(left)
            for j in left_result:
                result.append([nums[i]]+j)
    return result
