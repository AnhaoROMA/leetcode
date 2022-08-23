"""
https://leetcode.com/problems/word-break/

Given a string s and a dictionary of strings wordDict,
return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
"""


def word_break(s: str, word_dict: list[str]) -> bool:
    word_dict = set(word_dict)
    length = len(s)
    dp = [[False for _ in range(length)] for _ in range(length)]
    for n in range(length+1):
        for i in range(length-n+1):
            if s[i:i+n] in word_dict:
                dp[i][i+n-1] = True
                continue
            else:
                for j in range(i, i+n-1):
                    if dp[i][j] and dp[j+1][i+n-1]:
                        dp[i][i+n-1] = True
                        break
    return dp[0][length-1]


print(word_break("leetcode", ["leet", "code"]))
print(word_break("applepenapple", ["apple", "pen"]))
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))
