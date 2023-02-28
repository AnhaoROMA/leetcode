"""
https://leetcode.com/problems/reverse-pairs/

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where:
    (1) 0 <= i < j < nums.length
    (2) nums[i] > 2 * nums[j]

Input: nums = [1,3,2,3,1]
Output: 2
Explanation:
    The reverse pairs are:
        (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
        (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1

Input: nums = [2,4,3,5,1]
Output: 3
Explanation:
    The reverse pairs are:
        (1, 4) --> nums[1] = 4, nums[4] = 1, 4 > 2 * 1
        (2, 4) --> nums[2] = 3, nums[4] = 1, 3 > 2 * 1
        (3, 4) --> nums[3] = 5, nums[4] = 1, 5 > 2 * 1

Constraints:
    1 <= nums.length <= 5 * 10^4
    -2^{31} <= nums[i] <= 2^{31} - 1
"""


def reverse_pairs(nums: list[int]) -> int:
    """
    最 brute force 的解法是 i、j 双指针法，复杂度为 O(n^2) 。
    本题的 size 为 10^4 级别，故此法不通！

    我的想法是，设置数组 leftovers ，记录某元素的 ” 身后 “ 还有哪些元素。
    这样的复杂度即为 O(nlogn) 。
    """

    leftovers = nums[:]
    leftovers.sort()

    answer = 0
    for num in nums:
        #
        # 先更新 leftovers （去掉本身） 。
        # 主要是防止 负数 的情形。
        #
        i = 0
        j = len(leftovers) - 1
        while i < j:
            k = (i + j) // 2
            if leftovers[k] < num:
                i = k + 1
            elif leftovers[k] > num:
                j = k - 1
            else:
                i = k
                break
        leftovers.pop(i)
        #
        # 再找出某元素可构造多少对。
        #
        target = (num - 1) // 2
        i = 0
        j = len(leftovers)
        while i < j:
            k = (i + j) // 2
            if leftovers[k] <= target:
                i = k + 1
            else:
                j = k
        answer += j
    return answer


print(reverse_pairs([-5, -5]))
print(reverse_pairs([1, 3, 2, 3, 1]))
print(reverse_pairs([2, 4, 3, 5, 1]))
