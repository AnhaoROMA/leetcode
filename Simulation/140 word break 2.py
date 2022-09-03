"""
https://leetcode.com/problems/word-break-ii/

Given a string s and a dictionary of strings wordDict,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
"""


def word_break(s: str, word_dict: list[str]) -> list[str]:
    word_dict = set(word_dict)
    length = len(s)
    dp = [
        [
            [] for _ in range(length)
        ] for _ in range(length)
    ]
    for n in range(length+1):
        for i in range(length-n+1):
            if s[i:i+n] in word_dict:
                dp[i][i+n-1].append(s[i:i+n])
            for j in range(i, i+n-1):
                if dp[i][j] and dp[j+1][i+n-1]:
                    for left in dp[i][j]:
                        for right in dp[j+1][i+n-1]:
                            if left + " " + right not in dp[i][i+n-1]:
                                dp[i][i+n-1].append(left + " " + right)
    return dp[0][length-1]


print(word_break("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
