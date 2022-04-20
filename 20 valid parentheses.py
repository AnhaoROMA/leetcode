"""
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


def if_valid(string) -> bool:
    stack = list()
    for s in string:
        if s in ["(", "[", "{"]:
            if s == "(":
                stack.append(s)
            elif s == "[":
                stack.append(s)
            else:
                """
                s == "{"
                """
                stack.append(s)
        else:
            """
            s in [")", "]", "}"]
            """
            if len(stack) == 0:
                return False
            if s == ")":
                t = stack.pop()
                if t != "(":
                    return False
            elif s == "]":
                t = stack.pop()
                if t != "[":
                    return False
            else:
                """
                s == "}"
                """
                t = stack.pop()
                if t != "{":
                    return False
    if len(stack) != 0:
        return False
    else:
        return True


x = "()[]{}"
print(if_valid(x))
