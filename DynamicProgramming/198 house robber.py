"""
https://leetcode.com/problems/house-robber/

You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that
adjacent houses have security systems connected
and it will automatically contact the police
if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

# solution: 对于每一个点，只有 选 与 不选 两个选择。


# def rob(houses: list[int]) -> int:
#     if len(houses) == 1:
#         return houses[0]
#     elif len(houses) == 2:
#         return max(houses[0], houses[1])
#     else:
#         return max(houses[0] + rob(houses[2:]), rob(houses[1:]))

def rob(houses: list[int]) -> int:
    if len(houses) == 1:
        return houses[0]
    elif len(houses) == 2:
        return max(houses[0], houses[1])
    result_list = list()
    result_list.append(houses[0])
    result_list.append(max(houses[0], houses[1]))
    for i in range(2, len(houses)):
        result_list.append(max(result_list[-1], result_list[-2]+houses[i]))
    return result_list[-1]


nums = [2, 7, 9, 3, 1]
print(rob(nums))
