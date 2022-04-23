"""
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
"""


def rotate_image(matrix):
    length = len(matrix)
    pointer = 0
    while length > 1:
        for i in range(length-1):
            # print(matrix[pointer][pointer + i])
            # print(matrix[pointer + i][pointer + length - 1])
            # print(matrix[pointer + length - 1][pointer + length - 1 - i])
            # print(matrix[pointer + length - 1 - i][pointer])
            temp = matrix[pointer][pointer + i]
            matrix[pointer][pointer + i] = matrix[pointer + length - 1 - i][pointer]
            matrix[pointer + length - 1 - i][pointer] = matrix[pointer + length - 1][pointer + length - 1 - i]
            matrix[pointer + length - 1][pointer + length - 1 - i] = matrix[pointer + i][pointer + length - 1]
            matrix[pointer + i][pointer + length - 1] = temp
        pointer += 1
        length -= 2
    return matrix


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
print(rotate_image(matrix))