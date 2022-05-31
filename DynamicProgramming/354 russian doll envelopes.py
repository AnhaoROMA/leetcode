"""
https://leetcode.com/problems/russian-doll-envelopes/

You are given a 2D array of integers envelopes
where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if
both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1
"""

# A TLE solution:
# DP
#
# def russian_doll(envelopes: list[list[int]]) -> int:
#     envelopes.sort()
#     length = len(envelopes)
#     result_list = [1 for _ in range(length)]
#     for i in range(length):
#         for j in range(i):
#             if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
#                 result_list[i] = max(1 + result_list[j], result_list[i])
#     return max(result_list)


# 参考第300题（LIS）


def bin_search(target_list, target_value) -> int:
    start = 0
    end = len(target_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if target_list[mid] == target_value:
            return mid
        elif target_list[mid] > target_value:
            end = mid - 1
        else:
            start = mid + 1
    return start


def lis(nums: list[int]) -> int:
    result = list()
    result.append(nums[0])
    length = len(nums)
    i = 1
    while i < length:
        if nums[i] > result[-1]:
            result.append(nums[i])
        else:
            substitute_index = bin_search(result, nums[i])
            result[substitute_index] = nums[i]
        i += 1
    return len(result)


def russian_doll(envelopes: list[list[int]]) -> int:
    envelopes.sort(key=lambda x: (x[0], -1*x[1]))
    target_list = list()
    for item in envelopes:
        target_list.append(item[1])
    return lis(target_list)


a = [[5, 4], [6, 4], [6, 7], [2, 3]]
b = [[46, 89], [50, 53], [52, 68], [72, 45], [77, 81]]
c = [[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]]
print(russian_doll(c))
