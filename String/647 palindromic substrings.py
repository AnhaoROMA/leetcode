"""
https://leetcode.com/problems/palindromic-substrings/

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""


def cal(s: str) -> int:
    length = len(s)
    judge_table = [[False for _ in range(length)] for _ in range(length)]
    for i in range(length):
        judge_table[i][i] = True

    step = 1
    while step < length:
        for i in range(length):
            if i + step >= length:
                break
            if step == 1:
                judge_table[i][i + step] = (s[i] == s[i + step])
            else:
                judge_table[i][i + step] = (
                        (s[i] == s[i + step]) and judge_table[i + 1][i + step - 1]
                )
        step += 1
    print(judge_table)
    result = 0
    for i in range(length):
        for j in range(i, length):
            if judge_table[i][j] is True:
                result += 1
    return result


a = "aaaaa"
print(cal(a))
