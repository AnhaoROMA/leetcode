"""
https://leetcode.com/problems/jump-game-vi/

You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0.
In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1).
Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0

Constraints:
    1 <= nums.length, k <= 105
    -10^4 <= nums[i] <= 10^4
"""


# solution: 递归（TLE） / 动态规划（最值问题的思路之一，TLE）
def main(nums: list[int], k: int) -> int:
    length = len(nums)
    dp = [-1*10**-10 for _ in range(length)]
    dp[-1] = nums[-1]
    i = length - 2
    while i >= 0:
        dp[i] = nums[i] + dp[i+1]

        # dp[i] = max(
        #     dp[i], nums[i]+dp[i+1], nums[i]+dp[i+2], ... , nums[i]+dp[i+k]
        # )
        for j in range(1, min(k, length-1-i)+1):
            dp[i] = max(dp[i], nums[i]+dp[i+j])

        i -= 1
    return dp[0]


print(main([1, -1, -2, 4, -7, 3], 2))
print(main([10, -5, -2, 4, 0, 3], 3))
print(main([1, -5, -20, 4, -1, 3, -6, -3], 2))
