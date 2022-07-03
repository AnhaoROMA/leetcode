"""
https://leetcode.com/problems/search-a-2d-matrix-ii/

Write an efficient algorithm
that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.
"""


# solution：二分法
def search(matrix: list[list[int]], target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    # 第一次二分法
    i = 0
    j = m - 1
    while i < j:
        mid = (i + j) // 2 + 1
        if matrix[mid][0] == target:
            return True
        elif matrix[mid][0] < target:
            i = mid
        else:
            j = mid - 1
    r = i
    # print(row)
    # 第二次二分法
    for row in range(r+1):
        i = 0
        j = n - 1
        while i < j:
            mid = (i + j) // 2 + 1
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                i = mid
            else:
                j = mid - 1
        if matrix[row][i] == target:
            return True
    return False


print(
    search(
        [
            [1, 4, 7, 11, 15],
            [2, 5, 8, 12, 19],
            [3, 6, 9, 16, 22],
            [10, 13, 14, 17, 24],
            [18, 21, 23, 26, 30]
        ],
        0
    )
)