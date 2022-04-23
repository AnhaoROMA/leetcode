"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

"""
Input: nums = [3,2,4], target = 6
Output: [1,2]
"""

"""
Input: nums = [3,3], target = 6
Output: [0,1]
"""


# solution:
# create a hashmap
# for each_num in []:
#     to_find = target - each_num
#     if to_find in hashmap:
#         return
#     else:
#         add each_num to hashmap


def two_sum(array, target) -> list[int]:
    hashmap = dict()
    for i in range(len(array)):
        each_num = array[i]
        to_find = target - each_num
        if to_find in hashmap:
            return [hashmap[to_find], i]
        else:
            hashmap[each_num] = i


array = [2, 7, 11, 15]
target = 9
print(two_sum(array, target))
