"""
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/

Given an m x n matrix matrix and an integer k,
return the max sum of a rectangle in the matrix such that its sum is no larger than k.

It is guaranteed that there will be a rectangle with a sum no larger than k.
"""


def max_sum(matrix: list[list[int]], k: int) -> int:
    """
    前缀和、将二维问题简化为一维问题
    """
    m = len(matrix)
    n = len(matrix[0])

    def helping_hand(array: list[int]) -> int:
        tmp_array = []
        for num in array:
            tmp_array.append(num)
        for i in range(n):
            last_number = tmp_array[i]
            for j in range(i+1, n):
                tmp_array.append(last_number + tmp_array[j])
                last_number += tmp_array[j]
        tmp_array.sort()
        i = 0
        j = len(tmp_array) - 1
        while i < j:
            mid = (i + j + 1) // 2
            if tmp_array[mid] <= k:
                i = mid
            else:
                j = mid - 1
        return tmp_array[i]

    result = -1*10**5
    for top_row in range(m):
        temp = [0] * n
        for bottom_row in range(top_row, m):
            temp = temp[:n]
            for col in range(n):
                temp[col] += matrix[bottom_row][col]
            temp_result = helping_hand(temp)
            if temp_result <= k:
                result = max(result, temp_result)

    return result


print(
    max_sum(
        [
            [1,  0, 1],
            [0, -2, 3]
        ],
        2
    )
)
print(
    max_sum(
        [
            [5,  -4, -3, 4],
            [-3, -4, 4,  5],
            [5,  1,  5, -4]
        ],
        3
    )
)
