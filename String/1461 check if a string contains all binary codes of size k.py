"""
https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

Given a binary string s and an integer k,
return true if every binary code of length k is a substring of s.
Otherwise, return false.

Input: s = "00110110", k = 2
Output: true

Input: s = "0110", k = 1
Output: true

Input: s = "0110", k = 2
Output: false
"""


# 第一想法：把长度为 K 的所有二进制全部找出来，然后判断是否都在 s 中出现了。（TLE）
def has_all_codes(s: str, k: int) -> bool:
    permutation = ["0", "1"]
    while k > 1:
        new = list()
        while permutation:
            temp = permutation.pop()
            new.append(temp + "0")
            new.append(temp + "1")
        permutation = new
        k -= 1
    for sub_string in permutation:
        if sub_string not in s:
            return False
    return True


# 反过来想， s 中长度为 K 的所有不同的子串数目是否有 2 ^ K 个呢。
# 如果是的话，说明 s 中包含所有长度为 K 的二进制子串。
#
# 代码是 set + 子字符串 实现的。
def solution(s: str, k: int) -> bool:
    contains = set()
    length = len(s)
    for i in range(length-k+1):
        contains.add(s[i:i+k])
    return len(contains) == 2**k
