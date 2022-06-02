"""
https://leetcode.com/problems/spiral-matrix-ii/
"""


# solution:
# 不同于第 54 题的解法，我这次改用了剥皮法
def spiral(n: int) -> list[list[int]]:
    result = [[0 for _ in range(n)] for _ in range(n)]
    circles = (n + 1) // 2
    num = 1
    for circle in range(circles):
        i = circle
        j = circle
        while j < n - circle:
            # print((i, j))
            result[i][j] = num
            num += 1
            j += 1
        i = circle + 1
        while i < n - circle:
            # print((i, n - circle - 1))
            result[i][n-circle-1] = num
            num += 1
            i += 1
        j = n - circle - 1 - 1
        while j >= circle:
            # print((n - circle - 1, j))
            result[n-circle-1][j] = num
            num += 1
            j -= 1
        i = n - circle - 1 - 1
        while i > circle:
            # print((i, circle))
            result[i][circle] = num
            num += 1
            i -= 1
    return result


print(spiral(1))
