"""
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/

You are given an integer array nums and an integer x.
In one operation,
you can either remove the leftmost or the rightmost element from the array nums
and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it is possible,
otherwise, return -1.

Input: nums = [1,1,4,2,3], x = 5
Output: 2

Input: nums = [5,6,7,8,9], x = 4
Output: -1

Input: nums = [3,2,20,1,1,3], x = 10
Output: 5
"""


# TLE
def solution_1(nums: list[int], x: int) -> int:
    dfs = [
        [nums, 0, x]
    ]
    while dfs:
        temp_number, temp_result, leftovers = dfs.pop(0)
        if leftovers == 0:
            return temp_result
        if len(temp_number) == 0:
            continue
        if len(temp_number) == 1:
            if leftovers >= temp_number[0]:
                dfs.append(
                    [temp_number[1:], temp_result + 1, leftovers - temp_number[0]]
                )
            continue
        if leftovers >= temp_number[0]:
            dfs.append(
                [temp_number[1:], temp_result + 1, leftovers - temp_number[0]]
            )
        if leftovers >= temp_number[-1]:
            dfs.append(
                [temp_number[:-1], temp_result + 1, leftovers - temp_number[-1]]
            )
    return -1


# 滑动窗口（参考第 76 题）
# 实际上，我们也可以逆向思考。即：我们剩下的数组一定是原数组的中间部分。
# 就是说，我们只要知道数据中子序和等于 sum(nums) - x 的长度，再用 nums 的长度减去它就好了。
# 由于我们的目标是最小操作数，因此我们只要求和为定值的最长子序列，这是一个典型的滑动窗口问题。
def solution_2(nums: list[int], x: int) -> int:
    length = len(nums)
    result = length + 1

    target = sum(nums) - x
    if target == 0:
        return length

    temp = 0
    i = 0
    j = 0
    while j < length:
        temp += nums[j]
        while i < j and temp > target:
            temp -= nums[i]
            i += 1
        if temp == target:
            result = min(result, length-(j-i+1))
        j += 1

    if result == length + 1:
        return -1
    else:
        return result


print(solution_2([1, 1, 4, 2, 3], 5))
print(solution_2([3, 2, 20, 1, 1, 3], 10))
print(
    solution_2(
        [
            8828, 9581, 49, 9818, 9974,
            9869, 9991, 10000, 10000, 10000,
            9999, 9993, 9904, 8819, 1231,
            6309
        ],
        134365
    )
)
