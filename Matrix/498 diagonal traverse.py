"""
https://leetcode.com/problems/diagonal-traverse/

Given an m x n matrix mat,
return an array of all the elements of the array in a diagonal order.

Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= m, n <= 10^4
    1 <= m * n <= 10^4
    -10^5 <= mat[i][j] <= 10^5
"""


def diagonal_traverse(mat: list[list[int]]) -> list[int]:
    ans = list()

    m = len(mat)
    n = len(mat[0])
    how_many_diags = m + n - 1
    direction = True  # True：从左下向右上
    for k in range(how_many_diags):
        if direction:
            i = min(k, m-1)
            j = k - i
            while i >= 0 and j < n:
                ans.append(mat[i][j])
                i -= 1
                j += 1
        else:
            j = min(k, n-1)
            i = k - j
            while i < m and j >= 0:
                ans.append(mat[i][j])
                i += 1
                j -= 1
        direction = not direction

    return ans


print(
    diagonal_traverse(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )
)
