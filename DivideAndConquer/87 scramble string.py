"""
https://leetcode.com/problems/scramble-string/

We can scramble a string s to get a string t using the following algorithm:
    If the length of the string is 1, stop.
    If the length of the string is > 1, do the following:
        Split the string into two non-empty substrings at a random index,
            i.e., if the string is s, divide it to x and y where s = x + y.
        Randomly decide to swap the two substrings or to keep them in the same order.
            i.e., after this step, s may become s = x + y or s = y + x.
        Apply step 1 recursively on each of the two substrings x and y.

Given two strings s1 and s2 of the same length,
return true if s2 is a scrambled string of s1,
otherwise,
return false.

Input: s1 = "great", s2 = "rgeat"
Output: true

Input: s1 = "abcde", s2 = "caebd"
Output: false

Input: s1 = "a", s2 = "a"
Output: true

Constraints:
    s1.length == s2.length
    1 <= s1.length <= 30
    s1 and s2 consist of lowercase English letters.
"""

from collections import Counter


memory = {}


def scramble_string(s1: str, s2: str) -> bool:
    if s1 == s2:
        # 如果 s1 与 s2 相同，则返回 True 。
        return True
    if len(s1) == 1:
        # 如果 s1 与 s2 都只是单个字符、且不相同，则返回 False 。
        return False
    # 判断 s1 与 s2 有没有可能“扯上关系”。
    if Counter(s1) != Counter(s2):
        return False
    else:
        if (s1, s2) in memory:
            return memory[(s1, s2)]
        length = len(s1)
        for i in range(1, length):
            if scramble_string(s1[:i], s2[:i]) is True and scramble_string(s1[i:], s2[i:]) is True:
                memory[(s1, s2)] = True
                return True
            if scramble_string(s1[:i], s2[length-i:]) is True and scramble_string(s1[i:], s2[:length-i]) is True:
                memory[(s1, s2)] = True
                return True
        memory[(s1, s2)] = False
        return False


print(scramble_string("great", "rgeat"))
print(scramble_string("abcde", "caebd"))
print(scramble_string("a", "a"))
print(scramble_string("abcdefghijklmnopqrstuvwxyz", "abcdnopqrstuvwxyzefghijklm"))
print(scramble_string("abcdefghijklmnopqrstuvwxyz", "opqrstuvwxyzabcdefghijklmn"))
print(scramble_string("abcdefghiccccjklmnopqrstuvwxyz", "opqrstuvwccccxyzabcdefghijklmn"))
print(scramble_string("eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd"))
