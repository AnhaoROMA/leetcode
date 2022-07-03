"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a 1-indexed array of integers numbers
that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2]
where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2.

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2.
"""


def binary_search(nums: list[int], index, target) -> int:
    right = len(nums) - 1
    left = index + 1
    while left < right:
        middle = int((left + right + 1)/2)
        if nums[middle] == target:
            return middle
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle
    if nums[left] == target:
        return left
    else:
        return -1


def solution(numbers: list[int], target: int) -> list[int]:
    length = len(numbers)
    for i in range(length-1):
        leftovers = target - numbers[i]
        where = binary_search(numbers, i, leftovers)
        if where < 0:
            continue
        else:
            return [i+1, where+1]


def solution_2(numbers: list[int], target: int) -> list[int]:
    left = 0
    right = len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return [left+1, right+1]
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1
    return []


print(solution_2([2, 7, 11, 15], 9))
print(solution_2([2, 3, 4], 6))
print(solution_2([-1, 0], -1))
