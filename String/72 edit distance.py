"""
https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2,
return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character

Input:
word1 = "horse", word2 = "ros"
Output:
3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Input:
word1 = "intention", word2 = "execution"
Output:
5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""
MAX_VALUE = 500


def edit_distance(word_1: str, word_2: str) -> int:
    len_1 = len(word_1)
    len_2 = len(word_2)
    dp = [[MAX_VALUE for _ in range(len_2+1)] for _ in range(len_1+1)]
    for i in range(len_1+1):
        dp[i][0] = i
    for j in range(len_2+1):
        dp[0][j] = j
    for i in range(1, len_1+1):
        for j in range(1, len_2+1):
            if word_1[i-1] == word_2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j-1],
                    dp[i][j-1],
                    dp[i-1][j]
                )
    return dp[len_1][len_2]


a_1 = "horse"
a_2 = "ros"
b_1 = "intention"
b_2 = "execution"
print(edit_distance(a_1, a_2))
print(edit_distance(a_2, a_1))
print(edit_distance(b_1, b_2))
print(edit_distance(b_2, b_1))
