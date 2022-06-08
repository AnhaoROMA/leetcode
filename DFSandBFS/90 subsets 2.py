"""
https://leetcode.com/problems/subsets-ii/

Given an integer array nums that may contain duplicates,
return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
Return the solution in any order.

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Input: nums = [0]
Output: [[],[0]]

Constraints:
    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
"""


def subsets(nums: list[int]) -> list[list[int]]:
    nums.sort()

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
            if temp_list + [left_nums[i]] not in result:
                result.append(temp_list + [left_nums[i]])
            bfs.append(
                [temp_list + [left_nums[i]], left_nums[i+1:]]
            )

    return result


a = [1, 2, 2]
print(subsets(a))
