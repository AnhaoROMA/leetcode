"""
https://leetcode.com/problems/sliding-window-maximum/

You are given an array of integers nums,
there is a sliding window of size k
    which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Input: nums = [1], k = 1
Output: [1]

Constraints:
    1 <= nums.length <= 10^5
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
"""


def sliding_window(nums: list[int], k: int) -> list[int]:
    ans = list()

    index_list = list()
    for i in range(len(nums)):
        while index_list and nums[i] >= nums[index_list[-1]]:
            index_list.pop()
        while index_list and i-index_list[0] >= k:
            index_list.pop(0)
        index_list.append(i)
        ans.append(nums[index_list[0]])

    for _ in range(k-1):
        ans.pop(0)

    return ans


print(sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
print(sliding_window([1, 3, 1, 2, 0, 5], 3))
print(sliding_window([9, 10, 9, -7, -4, -8, 2, -6], 5))
