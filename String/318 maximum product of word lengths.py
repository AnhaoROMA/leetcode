"""
https://leetcode.com/problems/maximum-product-of-word-lengths/

Given a string array words,
return the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters.
If no such two words exist, return 0.

Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
"""


def common_element(a: str, b: str) -> bool:
    if set(a) & set(b):
        return True
    else:
        return False


def solution(strs: list[str]) -> int:
    result = 0
    length = len(strs)
    for i in range(length - 1):
        for j in range(i, length):
            if common_element(strs[i], strs[j]):
                continue
            else:
                result = max(result, len(strs[i])*len(strs[j]))
    return result
