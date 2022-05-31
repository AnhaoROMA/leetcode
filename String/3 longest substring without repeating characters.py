"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
"""

"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

"""
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""

"""
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


def solution(s: str) -> int:
    length = len(s)
    if length == 0:
        return 0
    result = 1

    i = 0
    while i < length:
        j = i + 1
        cache = [s[i]]
        while j < length and s[j] not in cache:
            cache.append(s[j])
            j += 1

        if j - i > result:
            result = j - i
        if j == length:
            break
        i = i + cache.index(s[j]) + 1
    return result


string = "au"
print(solution(string))
