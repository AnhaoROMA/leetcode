"""
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers
    where every element appears exactly twice,
except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^5
"""


def singleNonDuplicate(nums: list[int]) -> int:
    """
    由题意，这里对输入 nums[] 的要求是：
        nums[] 必须含有 singleNonDuplicate ，也就是说，len(nums) 一定是奇数。
    """
    length = len(nums)
    if length == 1:
        return nums[0]
    if length == 3:
        if nums[0] == nums[1]:
            return nums[2]
        else:
            # nums[2] == nums[1]:
            return nums[0]
    i = length // 2
    if nums[i] == nums[i+1]:
        # 1  1  2  3 |  3  4  4
        #          i | i+1
        # 需要剪枝（在 i-1 的位置剪，左枝有 i-1 个）
        # 1  1   2  |  3  3  4  4
        #       i-1
        if i % 2 == 0:
            return singleNonDuplicate(nums[i:])
        else:
            return singleNonDuplicate(nums[:i])
    else:
        # 1  1  2  3  3 |  4  4  8  8
        #             i | i+1
        if i % 2 == 0:
            return singleNonDuplicate(nums[:i+1])
        else:
            return singleNonDuplicate(nums[i+1:])


print(singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(singleNonDuplicate([1, 1, 3, 3, 4, 4, 8, 8, 9]))
print(singleNonDuplicate([1, 2, 2, 3, 3]))
