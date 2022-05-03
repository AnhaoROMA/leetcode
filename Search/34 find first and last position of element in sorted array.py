"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


def solution(nums: list[int], target: int) -> list[int]:
    length = len(nums)
    left = 0
    right = length - 1
    while (left < length and nums[left] < target) or (right > -1 and nums[right] > target):
        if nums[left] < target:
            left += 1
        if nums[right] > target:
            right -= 1
    if left > right:
        return [-1, -1]
    else:
        return [left, right]


a = [5, 7, 7, 8, 8, 10]
t = 7
print(solution(nums=a, target=t))

# another solution
# public int[] searchRange(int[] nums, int target) {
#     int start = 0;
#     int end = nums.length - 1;
#     int[] ans = { -1, -1 };
#     if (nums.length == 0) {
#         return ans;
#     }
#     while (start <= end) {
#         int mid = (start + end) / 2;
#         if (target == nums[mid]) {
#             end = mid - 1;
#         } else if (target < nums[mid]) {
#             end = mid - 1;
#         } else {
#             start = mid + 1;
#         }
#     }
#     //考虑 tartget 是否存在，判断我们要找的值是否等于 target 并且是否越界
#     if (start == nums.length || nums[ start ] != target) {
#         return ans;
#     } else {
#         ans[0] = start;
#     }
#     ans[0] = start;
#     start = 0;
#     end = nums.length - 1;
#     while (start <= end) {
#         int mid = (start + end) / 2;
#         if (target == nums[mid]) {
#             start = mid + 1;
#         } else if (target < nums[mid]) {
#             end = mid - 1;
#         } else {
#             start = mid + 1;
#         }
#     }
#     ans[1] = end;
#     return ans;
# }
