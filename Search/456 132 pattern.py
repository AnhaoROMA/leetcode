"""
https://leetcode.com/problems/132-pattern/

Given an array of n integers nums,
a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k]
such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
"""


# 解法一： 暴力法
def search(nums: list[int]) -> bool:
    length = len(nums)
    i = 0
    while i < length:
        k = i + 2
        while k < length:
            if nums[k] <= nums[i]:
                k += 1
            else:
                # nums[k] > nums[i]
                j = i + 1
                while j < k:
                    if nums[j] > nums[k]:
                        # nums[j] > nums[k] > nums[i]
                        return True
                    else:
                        j += 1
                k += 1
        i += 1
    return False


# 解法二： 单调栈的使用
def find(nums: list[int]) -> bool:
    length = len(nums)
    stack = list()
    third = -1 * 10 ** 9 - 1
    i = length - 1
    while i >= 0:
        if nums[i] < third:
            return True
        while len(stack) > 0 and stack[-1] < nums[i]:
            third = stack[-1]
            stack.pop()
        stack.append(nums[i])
        i -= 1
    return False


a2 = [1, 2, 3, 4]
a3 = [3, 1, 4, 2]
print(find(nums=a2))
