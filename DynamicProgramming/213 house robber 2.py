"""
https://leetcode.com/problems/house-robber-ii/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed.
All houses at this place are arranged in a circle.
That means the first house is the neighbor of the last one.
Meanwhile, adjacent houses have a security system connected,
and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
because they are adjacent houses.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [1,2,3]
Output: 3
"""


class Solution:
    def sub_rob(self, houses: list[int]) -> int:
        if len(houses) == 0:
            return 0
        elif len(houses) == 1:
            return houses[0]
        elif len(houses) == 2:
            return max(houses[0], houses[1])
        result_list = list()
        result_list.append(houses[0])
        result_list.append(max(houses[0], houses[1]))
        for i in range(2, len(houses)):
            result_list.append(max(result_list[-1], result_list[-2]+houses[i]))
        return result_list[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        sub_1 = nums[0: -1]
        sub_2 = nums[1:]
        return max(self.sub_rob(sub_1), self.sub_rob(sub_2))
