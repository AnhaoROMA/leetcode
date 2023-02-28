"""
https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/

Given an array of integers nums,
find the maximum length of a subarray where the product of all its elements is positive.

A subarray of an array is a consecutive sequence of zero or more values taken out of that array.

Return the maximum length of a subarray with positive product.

Input: nums = [1,-2,-3,4]
Output: 4
Explanation: The array nums already has a positive product of 24.

Input: nums = [-1,-2,-3,0,1]
Output: 2
Explanation: The longest subarray with positive product is [-1,-2] or [-2,-3].

Input: nums = [0,1,-2,-3,-4]
Output: 3
Explanation:
    The longest subarray with positive product is [1,-2,-3] which has a product of 6.
    Notice that we cannot include 0 in the subarray since that'll make the product 0 which is not positive.

Constraints:
    1 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
"""


def getMaxLen(nums: list[int]) -> int:
    """
    本题被归为 动态规划 类。

    对于数组中的每一个数，
        去求以它为结尾的 最长负子数组的长度（negative_max_length） 与 最长正子数组的长度（positive_max_length）。
    """
    num = nums[0]
    if num > 0:
        positive_max_length = 1
        negative_max_length = 0
    elif num < 0:
        positive_max_length = 0
        negative_max_length = 1
    else:
        positive_max_length = 0
        negative_max_length = 0
    result = positive_max_length
    for i in range(1, len(nums)):
        num = nums[i]
        if num > 0:
            if negative_max_length > 0:
                negative_max_length += 1
            positive_max_length += 1
        elif num < 0:
            if negative_max_length > 0:
                # negative_max_length = positive_max_length + 1
                # positive_max_length = negative_max_length - 1 + positive_max_length + 1
                negative_max_length, positive_max_length = positive_max_length+1, negative_max_length+1
            else:
                negative_max_length = positive_max_length + 1
                positive_max_length = 0
        else:
            positive_max_length = 0
            negative_max_length = 0
        result = max(result, positive_max_length)
    return result


print(getMaxLen([-1, -1, -1, 1, 1]))
print(getMaxLen([-7, -1, -7, 2, 2, -1, -4, 2, 2]))
print(getMaxLen([-1, 2]))
print(getMaxLen([1, 2, 3, 5, -6, 4, 0, 10]))
print(getMaxLen([1, -2, -3, 4]))
print(getMaxLen([-1, -2, -3, 0, 1]))
print(getMaxLen([0, 1, -2, -3, -4]))
