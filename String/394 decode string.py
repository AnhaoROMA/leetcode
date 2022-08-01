"""
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;
there are no extra white spaces, square brackets are well-formed, etc.
Furthermore,
you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 10^5.

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Input: s = "3[a2[c]]"
Output: "accaccacc"

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"

Constraints:
    1 <= s.length <= 30
    s consists of lowercase English letters, digits, and square brackets '[]'.
    s is guaranteed to be a valid input.
    All the integers in s are in the range [1, 300].
"""


def decode_string(s: str) -> str:
    if "[" not in s:
        return s
    length = len(s)
    for i in range(length):
        if s[i] == "[":
            break
    count = 0
    for j in range(i, length):
        if s[j] == "[":
            count += 1
        if s[j] == "]":
            count -= 1
            if count == 0:
                break
    k = i - 1
    while k >= 0:
        if s[k] not in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
            break
        k -= 1
    left_part = s[:k+1]
    midd_time = int(s[k+1:i])
    midd_part = s[i+1:j]
    rght_part = s[j+1:]
    return left_part + midd_time*decode_string(midd_part) + decode_string(rght_part)


print(decode_string("3[a]2[bc]"))
print(decode_string("3[a2[c]]"))
print(decode_string("2[abc]3[cd]ef"))
