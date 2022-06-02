"""
https://leetcode.com/problems/search-a-2d-matrix/

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
       target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
       target = 13
Output: false
"""


def bin_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left < right:
        middle = ((left + right) // 2) + 1
        if nums[middle] <= target:
            left = middle
        else:
            right = middle - 1
    return left


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    if matrix[0][0] > target:
        return False
    if matrix[-1][-1] < target:
        return False
    m = len(matrix)
    n = len(matrix[0])

    # bin-search
    top = 0
    down = m - 1
    while top < down:
        middle = ((top + down) // 2) + 1
        if matrix[middle][0] <= target:
            top = middle
        else:
            down = middle - 1
    x = top

    # bin-search
    left = 0
    right = n - 1
    while left < right:
        middle = ((left + right) // 2) + 1
        if matrix[x][middle] == target:
            return True
        elif matrix[x][middle] < target:
            left = middle
        else:
            right = middle - 1
    if matrix[x][left] == target:
        return True
    return False


a = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
b = [
    [1]
]
# print(search_matrix(a, 13))
print(search_matrix(b, 1))
