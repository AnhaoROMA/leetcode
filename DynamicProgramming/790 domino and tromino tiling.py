"""
https://leetcode.com/problems/domino-and-tromino-tiling/
"""


def numTilings(n: int) -> int:
    """
    一看就知道要使用动态规划。
    但是状态转移方程很难写。（本题先有转移方程，后有 dp 表的含义。）
    https://youtu.be/S-fUTfqrdq8
    """
    record = [[0 for _ in range(3)] for _ in range(n+1)]
    record[0][0] = 1
    record[1][0] = 1
    for i in range(2, n+1):
        record[i][0] = record[i-1][0] + record[i-2][0] + record[i-1][1] + record[i-1][2]
        record[i][1] = record[i-2][0] + record[i-1][2]
        record[i][2] = record[i-2][0] + record[i-1][1]
        # 注： record[i][1] === record[i][2] ！
    return record[n][0] % (10**9+7)


print(numTilings(4))
