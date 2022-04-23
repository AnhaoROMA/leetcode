"""
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

# 假如题目为：
# 有一个数组，数组内的元素代表点的坐标。请从中找出所有的等腰三角形。
#
# 解法为：先找顶点。


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = list()
        sum = 0
        length = len(nums)
        for i in range(length):
            target = sum - nums[i]
            hashmap = dict()
            for j in range(i+1, length):
                if target - nums[j] in hashmap:
                    temp = [nums[i], nums[hashmap[target - nums[j]]], nums[j]]
                    temp.sort()
                    if temp not in result:
                        result.append(temp)
                else:
                    hashmap[nums[j]] = j
        return result
