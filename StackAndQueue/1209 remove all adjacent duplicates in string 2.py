"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/

You are given a string s and an integer k,
a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them,
causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.
It is guaranteed that the answer is unique.
"""

"""
Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"
"""


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = list()
        for c in s:
            if len(stack) > 0 and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        result = ""
        for element in stack:
            for _ in range(element[1]):
                result += element[0]
        return result
