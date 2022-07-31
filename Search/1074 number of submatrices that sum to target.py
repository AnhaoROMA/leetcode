"""
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

Given a matrix and a target,
return the number of non-empty submatrices that sum to target.
"""


# 参考第 560 题
# 链接：https://www.jianshu.com/p/a15015a4d569
def solution(matrix: list[list[int]], target: int) -> int:
    m = len(matrix)
    n = len(matrix[0])
    # helping_hand[x][y] = sum(matrix[i][j]), where i <= x and j <= y
    helping_hand = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            helping_hand[i][j] = matrix[i][j]
            if i > 0:
                helping_hand[i][j] += helping_hand[i-1][j]
            if j > 0:
                helping_hand[i][j] += helping_hand[i][j-1]
            if i > 0 and j > 0:
                helping_hand[i][j] -= helping_hand[i-1][j-1]
    # print(helping_hand)
    # 固定上下边界和右边界
    # 上下边界与右边界所围成之区域的值为 cur = pre[buttom][right] - pre[top-1][right]
    # 在 hashmap 中查找 cur-target, 最终结果加上 hashmap[cur-target] 。
    # hashmap[cur-target] += 1
    ans = 0
    for top in range(m):
        for bottom in range(top, m):
            record = {
                0: 1
            }
            for right in range(n):
                if top > 0:
                    cur_sum = helping_hand[bottom][right] - helping_hand[top-1][right]
                else:
                    cur_sum = helping_hand[bottom][right]

                if cur_sum-target in record:
                    ans += record[cur_sum-target]
                if cur_sum in record:
                    record[cur_sum] += 1
                else:
                    record[cur_sum] = 1
    return ans


print(solution([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0))
print(solution([[1, -1], [-1, 1]], 0))
