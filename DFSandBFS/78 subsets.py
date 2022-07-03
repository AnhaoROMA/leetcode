"""
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Input: nums = [0]
Output: [[],[0]]
"""


def subsets(nums: list[int]) -> list[list[int]]:
    result = list()
    result.append([])

    bfs = list()
    bfs.append(
        [[], nums]
    )
    while bfs:
        temp_list, left_nums = bfs.pop(0)
        if len(left_nums) == 0:
            continue
        length = len(left_nums)
        for i in range(length):
            result.append(temp_list + [left_nums[i]])
            bfs.append(
                [temp_list + [left_nums[i]], left_nums[i+1:]]
            )

    return result


a = [1, 2, 3]
print(subsets(a))
