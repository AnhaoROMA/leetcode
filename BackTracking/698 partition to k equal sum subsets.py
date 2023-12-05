"""
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Given an integer array nums and an integer k,
return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
    Input: nums = [4,3,2,3,5,2,1], k = 4
    Output: true
    Explanation: It is possible to divide it into 4 subsets (5), (1,4), (2,3), (2,3) with equal sums.

Example 2:
    Input: nums = [1,2,3,4], k = 3
    Output: false

Constraints:
    1 <= k <= nums.length <= 16
    1 <= nums[i] <= 10^4
    The frequency of each element is in the range [1, 4].
"""


def canPartitionKSubsets(nums: list[int], k: int) -> bool:
    """
    回溯法
    """
    if sum(nums) % k != 0:
        return False
    target = sum(nums) // k
    if max(nums) > target:
        return False
    nums.sort(reverse=True)
    while nums and nums[0] == target:
        nums.pop(0)
        k -= 1

    def backtracking(participants: list[int], seats: list[int]) -> bool:
        if not participants:
            return True
        temp = participants.pop(0)
        visited = set()  # 避免重复尝试，如 8, 4, 1, 1, 1, 0, 0, 0 。
        for i in range(k):
            if seats[i] + temp <= target and seats[i] not in visited:
                visited.add(seats[i])
                seats[i] += temp
                if backtracking(participants, seats) is True:
                    return True
                seats[i] -= temp
        participants.insert(0, temp)
        return False

    return backtracking(
        participants=nums,
        seats=[0 for _ in range(k)]
    )


print(
    canPartitionKSubsets(
        [10,5,5,4,3,6,6,7,6,8,6,3,4,5,3,7],
        8
    )
)
print(
    canPartitionKSubsets(
        [3,9,4,5,8,8,7,9,3,6,2,10,10,4,10,2],
        10
    )
)
print(
    canPartitionKSubsets(
        [18,20,39,73,96,99,101,111,114,190,207,295,471,649,700,1037],
        4
    )
)
print(
    canPartitionKSubsets(
        [4,3,2,3,5,2,1],
        4
    )
)
print(
    canPartitionKSubsets(
        [5,2,4,1],
        3
    )
)
