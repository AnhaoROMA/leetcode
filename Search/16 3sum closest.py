"""
https://leetcode.com/problems/3sum-closest/

Given an integer array nums of length n and an integer target,
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""

"""
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Input: nums = [0,0,0], target = 1
Output: 0
"""


def closest(nums: list[int], target) -> int:
    nums.sort()
    length = len(nums)
    result = nums[0] + nums[1] + nums[2]

    for i in range(length-2):
        j = i + 1
        k = length - 1
        num1 = nums[i]
        while j < k:
            num2 = nums[j]
            num3 = nums[k]
            tmp = num1 + num2 + num3 - target
            if tmp > 0:
                if abs(tmp) < abs(result-target):
                    result = num1 + num2 + num3
                k -= 1
            elif tmp < 0:
                if abs(tmp) < abs(result-target):
                    result = num1 + num2 + num3
                j += 1
            else:
                return num1 + num2 + num3
    return result


a = [0, 1, 2]
print(closest(a, 3))
