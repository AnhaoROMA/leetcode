"""
https://leetcode.com/problems/longest-valid-parentheses/

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.
"""

"""
Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
"""


def longest(s: str) -> int:
    # length = len(s)
    # table = [i - 1 for i in range(length)]
    # i = 0
    # while i < length:
    #     stack = list()
    #     j = i
    #     while j < length:
    #         if s[j] == "(":
    #             stack.append("(")
    #         else:
    #             # s[j] == ")"
    #             if len(stack) == 0:
    #                 i = j + 1
    #                 break
    #             stack.pop()
    #             if len(stack) == 0:
    #                 table[i] = j
    #         j += 1
    #     i += 1
    # result = 0
    # for i in range(length):
    #     tmp = table[i] - i + 1
    #     if tmp > result:
    #         result = tmp
    # return result
    length = len(s)
    result = 0
    i = 0
    while i < length:
        stack = list()
        j = i
        while j < length:
            if s[j] == "(":
                stack.append("(")
            else:
                # s[j] == ")"
                if len(stack) == 0:
                    i = j
                    break
                stack.pop()
                if len(stack) == 0:
                    result = max(j - i + 1, result)
            j += 1
        i += 1
    return result


string = ")()())"
print(longest(s=string))
