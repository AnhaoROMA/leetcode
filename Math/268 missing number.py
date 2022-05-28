"""
https://leetcode.com/problems/missing-number/

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Input: nums = [3,0,1]
Output: 2

Input: nums = [0,1]
Output: 2

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
"""


# solution:
# 最直观的一个方法是用等差数列的求和公式求出0到n之间所有的数字之和，
# 然后再遍历数组算出给定数字的累积和，然后做减法，差值就是丢失的那个数字。
def find(nums: list[int]) -> int:
    n = len(nums)
    theory_sum = (1+n)*n/2
    practical_sum = sum(nums)
    return int(theory_sum - practical_sum)
