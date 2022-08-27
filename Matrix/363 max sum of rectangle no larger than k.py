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
    prefix_sum = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                prefix_sum[i][j] = matrix[i][j]
            else:
                prefix_sum[i][j] = prefix_sum[i-1][j] + matrix[i][j]
    result = -1*10**5
    for top_row in range(m):
        for bottom_row in range(top_row, m):
            temp = []
            for col in range(n):
                if top_row == 0:
                    val = prefix_sum[bottom_row][col]
                else:
                    val = prefix_sum[bottom_row][col] - prefix_sum[top_row-1][col]
                temp.append(val)
            length = len(temp)
            for i in range(length):
                last_number = temp[i]
                for j in range(i+1, length):
                    temp.append(last_number+temp[j])
                    last_number += temp[j]
            temp.sort()
            if temp[0] > k:
                continue
            i = 0
            j = len(temp) - 1
            while i < j:
                mid = (i+j+1)//2
                if temp[mid] <= k:
                    i = mid
                else:
                    j = mid - 1
            result = max(result, temp[i])
    return result


# print(
#     max_sum(
#         [
#             [1,  0, 1],
#             [0, -2, 3]
#         ],
#         2
#     )
# )
# print(
#     max_sum(
#         [
#             [5,  -4, -3, 4],
#             [-3, -4, 4,  5],
#             [5,  1,  5, -4]
#         ],
#         3
#     )
# )
print(max_sum([[27,5,-20,-9,1,26,1,12,7,-4,8,7,-1,5,8],[16,28,8,3,16,28,-10,-7,-5,-13,7,9,20,-9,26],[24,-14,20,23,25,-16,-15,8,8,-6,-14,-6,12,-19,-13],[28,13,-17,20,-3,-18,12,5,1,25,25,-14,22,17,12],[7,29,-12,5,-5,26,-5,10,-5,24,-9,-19,20,0,18],[-7,-11,-8,12,19,18,-15,17,7,-1,-11,-10,-1,25,17],[-3,-20,-20,-7,14,-12,22,1,-9,11,14,-16,-5,-12,14],[-20,-4,-17,3,3,-18,22,-13,-1,16,-11,29,17,-2,22],[23,-15,24,26,28,-13,10,18,-6,29,27,-19,-19,-8,0],[5,9,23,11,-4,-20,18,29,-6,-4,-11,21,-6,24,12],[13,16,0,-20,22,21,26,-3,15,14,26,17,19,20,-5],[15,1,22,-6,1,-9,0,21,12,27,5,8,8,18,-1],[15,29,13,6,-11,7,-6,27,22,18,22,-3,-9,20,14],[26,-6,12,-10,0,26,10,1,11,-10,-16,-18,29,8,-8],[-19,14,15,18,-10,24,-9,-7,-19,-14,23,23,17,-5,6]]
, -100))
