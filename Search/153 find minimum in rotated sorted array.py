"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""


def search(nums: list[int]) -> int:
    start = 0
    end = len(nums) - 1
    while end - start > 1:
        mid = (start + end) // 2
        if nums[start] < nums[mid] and nums[mid] > nums[end]:
            # 左侧是有序的，右侧是无序的
            start = mid
        elif nums[start] > nums[mid] and nums[mid] < nums[end]:
            # nums[start] > nums[mid]
            # 右侧是有序的，左侧是无序的
            end = mid
        else:
            # 已经有序
            return nums[start]
    return min(nums[start], nums[end])
