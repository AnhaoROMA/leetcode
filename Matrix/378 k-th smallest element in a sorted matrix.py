"""
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

Given an n x n matrix where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order,
not the kth distinct element.

You must find a solution with a memory complexity better than O(n^2).
"""


def kth_smallest(matrix: list[list[int]], k: int) -> int:
    """
    二分查找
    """
    n = len(matrix)

    def whether_possible(val: int) -> bool:
        """
        如果 小于等于 val 的元素的个数 大于等于 k，则 val 是可能的结果。
        为什么说可能呢？因为 val 未必是 matrix 的元素。
        但是如果 小于等于 val 的元素的个数 小于 k，则 val 不可能是结果。
        """
        count = 0
        for x in range(n):
            if matrix[x][0] > val:
                break
            for y in range(n):
                if matrix[x][y] > val:
                    break
                else:
                    count += 1
        return count >= k

    i = matrix[0][0]
    j = matrix[-1][-1]
    while i < j:
        m = (i + j) // 2
        if whether_possible(m):
            j = m
        else:
            i = m + 1
    return i


print(kth_smallest([[1, 2], [1, 3]], 2))
print(kth_smallest([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8))
