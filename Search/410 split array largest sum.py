"""
https://leetcode.com/problems/split-array-largest-sum/

Given an integer array nums and an integer k,
split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

Input:
    nums = [7,2,5,10,8], k = 2
Output:
    18
Explanation:
    There are four ways to split nums into two subarrays.
    The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is only 18.

Input:
    nums = [1,2,3,4,5], k = 2
Output:
    9
Explanation:
    There are four ways to split nums into two subarrays.
    The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is only 9.

Constraints:
    1 <= nums.length <= 1000
    0 <= nums[i] <= 10^6
    1 <= k <= min(50, nums.length)
"""


def splitArray(nums: list[int], k: int) -> int:
    """
    https://www.youtube.com/watch?v=YUF3_eBdzsk

    针对结果的二分查找
    """

    def canSplit(largest) -> bool:
        num_subarray = 0
        cur_sum = 0
        for n in nums:
            cur_sum += n
            if cur_sum > largest:
                num_subarray += 1
                cur_sum = n
        if num_subarray+1 > k:
            return False
        else:
            return True

    L = max(nums)
    R = sum(nums)
    ans = R
    while L <= R:
        M = (L+R)//2
        if canSplit(M) is True:
            ans = M
            R = M-1
        else:
            L = M+1

    return ans


print(
    splitArray(
        [1,2,3,4,5],
        2
    )
)
