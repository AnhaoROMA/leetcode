"""
https://leetcode.com/problems/number-of-matching-subsequences/

Given a string s and an array of strings words,
return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string
    generated from the original string
    with some characters (can be none) deleted
    without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2

Constraints:
    1 <= s.length <= 5 * 10^4
    1 <= words.length <= 5000
    1 <= words[i].length <= 50
    s and words[i] consist of only lowercase English letters.
"""


# 暴力解法，即一个一个地去判断，很明显会TLE。
# 解法：https://blog.csdn.net/qq_37821701/article/details/108532318
def count(s: str, words: list[str]) -> int:
    book = dict()

    for word in words:
        if word[0] in book:
            book[word[0]].append(word[1:])
        else:
            book[word[0]] = [word[1:]]

    res = 0
    for c in s:
        if c not in book:
            continue
        else:
            tmp = book[c]
            del book[c]
            for temp in tmp:
                if temp == "":
                    res += 1
                else:
                    if temp[0] in book:
                        book[temp[0]].append(temp[1:])
                    else:
                        book[temp[0]] = [temp[1:]]
    return res


print(count("abcde", ["a", "bb", "acd", "ace"]))
print(count("dsahjpjauf", ["ahjpjau", "ja", "ahbwzgqnuk", "tnmlanowax"]))
