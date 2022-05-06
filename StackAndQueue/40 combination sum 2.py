"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
    [1,1,6],
    [1,2,5],
    [1,7],
    [2,6]
]

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
    [1,2,2],
    [5]
]
"""


def dfs(a):
    result = list()
    temp_result = a[0]
    leftovers = a[1]
    left_target = a[2]
    for element in leftovers:
        if left_target - element >= 0:
            temp_result_next = temp_result + [element]

            leftovers_next = dict()
            for i in leftovers:
                leftovers_next[i] = leftovers[i]

            leftovers_next[element] -= 1
            if leftovers_next[element] == 0:
                del leftovers_next[element]
            left_target_next = left_target - element
            result.append([temp_result_next, leftovers_next, left_target_next])

        else:
            continue
    return result


def solution(nums: list[int], target: int) -> list[list[int]]:
    result = list()
    leftovers = dict()
    for element in nums:
        if element in leftovers:
            leftovers[element] += 1
        else:
            leftovers[element] = 1
    stack = [
        [
            [], leftovers, target
        ]
    ]
    while len(stack) != 0:
        temp = stack.pop()
        if temp[2] == 0:
            temp[0].sort()
            if temp[0] not in result:
                result.append(temp[0])
        else:
            possible = dfs(temp)
            for p in possible:
                stack.append(p)
    return result


c = [10, 1, 2, 7, 6, 1, 5]
target = 8
print(solution(nums=c, target=t))
