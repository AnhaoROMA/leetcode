"""
https://leetcode.com/problems/pascals-triangle-ii/
"""


def solution(n: int) -> list[list[int]]:
    result = list()
    row = 1
    result.append([1])
    while row < n + 1:
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
    return result[-1]


a = 3
print(solution(n=a))
