"""
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


def solution(matrix: list[list[int]]) -> list[int]:
    result = list()

    border_up = 0
    border_left = -1
    border_right = len(matrix[0])
    border_down = len(matrix)
    # print(border_up, border_down, border_left, border_right)

    i = 0
    j = 0
    direction = "right"
    result.append(matrix[i][j])
    while (border_down - border_up) + (border_right - border_left) > 2:
        if direction == "right":
            j += 1
            if j == border_right:
                j -= 1
                if i + 1 == border_down:
                    break
                direction = "down"
                border_right -= 1
            else:
                result.append(matrix[i][j])
        elif direction == "down":
            i += 1
            if i == border_down:
                i -= 1
                if j - 1 == border_left:
                    break
                direction = "left"
                border_down -= 1
            else:
                result.append(matrix[i][j])
        elif direction == "left":
            j -= 1
            if j == border_left:
                j += 1
                if i - 1 == border_up:
                    break
                direction = "up"
                border_left += 1
            else:
                result.append(matrix[i][j])
        else:
            # direction == "up"
            i -= 1
            if i == border_up:
                i += 1
                if j + 1 == border_right:
                    break
                direction = "right"
                border_up += 1
            else:
                result.append(matrix[i][j])

    return result


a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
b = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
c = [
    [6, 9, 7]
]
print(solution(matrix=b))
