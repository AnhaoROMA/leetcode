"""
https://leetcode.com/problems/palindrome-partitioning/description/

Given a string s, partition s such that
every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Input: s = "a"
Output: [["a"]]

Constraints:
    1 <= s.length <= 16
    s contains only lowercase English letters.
"""


def partition(s: str) -> list[list[str]]:
    """
    一开始想到的是分治法，但是当 s.length >= 15 时会 TLE 。
    """
    # def is_palindrome(sub_string: str) -> bool:
    #     if sub_string[::-1] == sub_string:
    #         return True
    #     else:
    #         return False
    #
    # def helper(sub_string: str):
    #     ans = set()
    #     if is_palindrome(sub_string) is True:
    #         ans.add(sub_string)
    #     for i in range(len(sub_string) - 1):
    #         left_part = sub_string[:i+1]
    #         right_part = sub_string[i+1:]
    #         left_ans = helper(left_part)
    #         right_ans = helper(right_part)
    #         for m in left_ans:
    #             for n in right_ans:
    #                 ans.add(m+"#"+n)
    #     return ans
    #
    # res = list()
    # for j in helper(s):
    #     res.append(j.split("#"))
    # return res

    """
    后来看别人的解法，发现用 回溯法/DFS 可以求解。
    """
    ans = list()
    length = len(s)

    def extend(i, cur):
        if i == length:
            ans.append(cur[::])
        else:
            p = ""
            for j in range(i, length):
                p += s[j]
                if p == p[::-1]:
                    extend(j+1, cur+[p])

    extend(0, [])
    return ans


print(partition("aab"))
print(partition("a"))
print(partition("ssssssssssssss"))
