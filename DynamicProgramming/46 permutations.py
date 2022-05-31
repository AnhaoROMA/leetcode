"""
https://leetcode.com/problems/permutations/

Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
"""

"""
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Input: nums = [1]
Output: [[1]]
"""


def permute(nums: list[int]) -> list[list[int]]:
    result = list()
    length = len(nums)
    if length == 1:
        result.append([nums[0]])
    elif length == 2:
        result.append([nums[0], nums[1]])
        result.append([nums[1], nums[0]])
    else:
        for i in range(length):
            left = nums[:i] + nums[i+1:]
            left_result = permute(left)
            for j in left_result:
                result.append([nums[i]]+j)
    return result


a = [1, 2, 3, 4]
print(permute(a))
