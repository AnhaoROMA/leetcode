"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.
"""


# solution 1: 暴力求解

# solution 2: 动态规划 + 哈希表
# hashmap[i][j] = hashmap[i-1][j-1] and (list[i] == list[j])
def solution_dp(s: str):
    length = len(s)
    # 注意浅拷贝的问题
    judge_table = [[False for _ in range(length)] for _ in range(length)]
    result_i = 0
    result_j = 0
    result_k = result_i - result_j + 1
    for i in range(length):
        for j in range(i):
            if i - j < 3:
                judge_table[i][j] = (s[i] == s[j])
            else:
                judge_table[i][j] = judge_table[i-1][j+1] and (s[i] == s[j])
            if judge_table[i][j] is True and i - j + 1 > result_k:
                result_i = i
                result_j = j
                result_k = result_i - result_j + 1
    return s[result_j: result_i+1]

# solution 3: Manacher算法
