"""
https://leetcode.com/problems/subarray-sum-equals-k/

Given an array of integers nums and an integer k,
return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

Input: nums = [1,1,1], k = 2
Output: 2

Input: nums = [1,2,3], k = 3
Output: 2

Constraints:
    1 <= nums.length <= 2 * 10^4
    -1000 <= nums[i] <= 1000
    -10^7 <= k <= 10^7
"""


# 我的想法：
# 设 temp[i] = sum(nums[:i+1])，则 sub_sum[i][j] = temp[j] - temp[i-1]
# 这样的复杂度为 n + n^2

# 复杂度为 n 的解法（前缀法）：
# 假设我们已知 sum(nums[:i+1])，
# 那么存不存在 j \in [0:i]，使得 sum(nums[:j]) == sum(nums[:i+1]) - k?
# 又存在几个这样的 j 呢？
def solution(nums: list[int], k: int) -> int:
    res = 0

    record = {0: 1}
    temp_sum = 0
    for num in nums:
        temp_sum += num
        if temp_sum - k in record:
            res += record[temp_sum - k]
        if temp_sum in record:
            record[temp_sum] += 1
        else:
            record[temp_sum] = 1

    return res


print(solution([1, 2, 3], 3))
print(solution([1], 0))
