"""
https://leetcode.com/problems/pascals-triangle/

Given an integer numRows, return the first numRows of Pascal's triangle.
"""


def solution(n: int) -> list[list[int]]:
    result = list()
    row = 1
    result.append([1])
    while row < n:
        last_result = result[row-1]
        row += 1
        temp_result = list()
        for i in range(row):
            if i - 1 < 0:
                left = 0
            else:
                left = last_result[i-1]
            if i > row - 2:
                right = 0
            else:
                right = last_result[i]
            temp_result.append(left+right)
        result.append(temp_result)
    return result


a = 5
print(solution(n=a))
