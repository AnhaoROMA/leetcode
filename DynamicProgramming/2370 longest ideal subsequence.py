"""
https://leetcode.com/problems/longest-ideal-subsequence/
"""


def longest(s: str, k: int) -> int:
    """
    letter[i] presents
    the longest length of ideal subsequences that end with letter i
    """
    letter = dict()
    for i in range(97, 123):
        letter[chr(i)] = 0
    # print(letter)
    for c in s:
        pos = ord(c)
        left = max(97, pos - k)
        right = min(122, pos + k)
        # print(left, right)
        letter[c] = max([letter[chr(i)] for i in range(left, right + 1)]) + 1
    return max(list(letter.values()))
