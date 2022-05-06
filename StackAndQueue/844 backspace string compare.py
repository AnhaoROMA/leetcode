"""
https://leetcode.com/problems/backspace-string-compare/

Given two strings s and t,
return true if they are equal when both are typed into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.
"""

"""
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
"""


def cin(s: str) -> str:
    stack = list()
    for char in s:
        if char != "#":
            stack.append(char)
        else:
            if len(stack) > 0:
                stack.pop()
    result = ""
    for element in stack:
        result += element
    return result


def compare(s: str, t: str) -> bool:
    s = cin(s)
    t = cin(t)
    if s == t:
        return True
    else:
        return False


string = "#ab#c"
target = "ad#c"
print(compare(string, target))
