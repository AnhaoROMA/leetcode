"""
https://leetcode.com/problems/maximum-erasure-value/

You are given an array of positive integers nums
and want to erase a subarray containing unique elements.
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a,
that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
"""


# 滑动窗口
def erase(nums: list[int]) -> int:
    length = len(nums)
    result = 0
    amount = 0
    i = 0
    j = 0
    window = set()
    while j < length:
        if nums[j] not in window:
            window.add(nums[j])
            amount += nums[j]
            j += 1
        else:
            result = max(result, amount)
            amount -= nums[i]
            window.remove(nums[i])
            i += 1
    result = max(result, amount)
    return result


print(erase([4, 2, 4, 5, 6]))
print(erase([5, 2, 1, 2, 5, 2, 1, 2, 5]))
