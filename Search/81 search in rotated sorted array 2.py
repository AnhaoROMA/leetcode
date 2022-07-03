"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/

There is an integer array nums sorted in non-decreasing order
(not necessarily with distinct values).

Before being passed to your function,
nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).

For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5
and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target,
return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
"""


#
# solution:
# 二分查找，详见代码中的注释。
#
def search(nums: list[int], target: int) -> bool:
    # 双指针，一个在开头，一个在结尾。
    left = 0
    right = len(nums) - 1
    #
    # 确定中间的指针 mid
    #
    # 错误的思路：
    #    如果 nums[mid] <= nums[right]，则证明数组的右侧是有序的。
    #    反之，右侧是无序的。
    # 错误的原因：
    #    假如某一侧为 [1, 1, 1, 1, 2, 1, 1, 1, 1, 1]，按照错误的思路，会误判为“有序”。
    #
    while left < right:
        mid = int((left + right + 1) / 2)
        if nums[mid] == target:
            return True
        #
        # 由于之前那道题不存在相同值，我们在比较中间值和最右值时就完全符合之前所说的规律：
        # 如果中间的数小于最右边的数，则右半段是有序的，若中间数大于最右边数，则左半段是有序的。
        #
        # 而如果可以有重复值，就会出现两种情况，[3 1 1] 和 [1 1 3 1]。
        # 对于这两种情况中间值等于最右值时，目标值3既可以在左边又可以在右边。
        #
        # 对于这种情况其实处理非常简单，只要把最右值向左一位即可继续循环。
        # 如果还相同则继续移，直到移到不同值为止。
        #
        if nums[mid] == nums[right]:
            right -= 1
        elif nums[mid] < nums[right]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    if nums[left] == target:
        return True
    else:
        return False


print(search([2, 5, 6, 0, 0, 1, 2], 0))
print(search([2, 5, 6, 0, 0, 1, 2], 3))
print(
    search(
        nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1],
        target=2
    )
)
print(search([1, 3, 5], 1))
print(search([3, 5, 1], 1))
