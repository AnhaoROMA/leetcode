"""
https://leetcode.com/problems/matchsticks-to-square/

You are given an integer array matchsticks
    where matchsticks[i] is the length of the ith matchstick.
You want to use all the matchsticks to make one square.
You should not break any stick,
but you can link them up,
and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

Input: matchsticks = [1,1,2,2,2]
Output: true

Input: matchsticks = [3,3,3,3,4]
Output: false
"""


#
# 错误的解法：
#
# def backtracking(choices: list[int], target: int, start: int) -> bool:
#     """
#     判断能否从 choices 这个数组中，找到和为 target 的子数组。
#     """
#     if target == 0:
#         return True
#     length = len(choices)
#     if start == length:
#         return False
#     for i in range(start, length):
#         temp = choices[i]
#         if temp > target:
#             continue
#         choices.pop(i)
#         new_choices = choices
#         if not backtracking(new_choices, target-temp, i):
#             choices.insert(i, temp)
#         else:
#             return True
#     return False
#
#
# def make_square(matchsticks: list[int]) -> bool:
#     if sum(matchsticks) % 4 != 0:
#         return False
#     matchsticks.sort(reverse=True)
#     target = sum(matchsticks) // 4
#     # 错误思路：分开考虑
#     for _ in range(4):
#         if not backtracking(matchsticks, target, 0):
#             return False
#     return True


def dfs(nums, index, target):
    if index == len(nums):
        return True
    num = nums[index]
    for i in range(4):
        if target[i] < nums[-1]:
            return False
        if target[i] >= num:
            target[i] -= num
            if dfs(nums, index + 1, target):
                return True
            target[i] += num
    return False


def make_square(nums):
    if not nums or len(nums) < 4:
        return False
    _sum = sum(nums)
    div, mod = divmod(_sum, 4)
    if mod != 0 or max(nums) > _sum // 4:
        return False
    nums.sort(reverse=True)
    target = [div] * 4
    return dfs(nums, 0, target)


# print(make_square([1, 1, 2, 2, 2]))
# print(make_square([5, 4, 3, 3, 2, 2, 1]))
# print(make_square([2, 2, 2, 2, 2, 6]))
# print(make_square([3, 3, 3, 3, 4]))
# print(make_square([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]))
# print(make_square([13, 11, 1, 8, 6, 7, 8, 8, 6, 7, 8, 9, 8]))
print(make_square([14, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 8, 9, 19]))
