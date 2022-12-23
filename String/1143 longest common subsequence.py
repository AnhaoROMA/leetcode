"""
https://leetcode.com/problems/longest-common-subsequence/description/
"""


def longest_common_subsequence(text_1: str, text_2: str) -> int:
    """
    说到最值问题，就应该想到动态规划。
    """
    # dp[i][j] := text_1[:i] 与 text_2[:j] 的最长公共子字符串
    length_1 = len(text_1)
    length_2 = len(text_2)
    dp_table = [[0 for _ in range(length_2+1)] for _ in range(length_1+1)]
    # 更新 dp 表
    for i in range(1, length_1+1):
        for j in range(1, length_2+1):
            if text_1[i-1] == text_2[j-1]:
                dp_table[i][j] = max(
                    dp_table[i-1][j-1] + 1,
                    dp_table[i][j-1],
                    dp_table[i-1][j]
                )
            else:
                dp_table[i][j] = max(
                    dp_table[i-1][j-1],
                    dp_table[i][j-1],
                    dp_table[i-1][j]
                )
    # print(dp_table)
    # 返回最终结果
    return dp_table[length_1][length_2]


print(
    longest_common_subsequence(
        "abcde",
        "ace"
    )
)
print(
    longest_common_subsequence(
        "abc",
        "abc"
    )
)
print(
    longest_common_subsequence(
        "abcde",
        "def"
    )
)
