"""
https://leetcode.com/problems/basic-calculator/

Given a string s representing a valid expression,
implement a basic calculator to evaluate it,
and return the result of the evaluation.

Note:
    You are not allowed to use any built-in function
    which evaluates strings as mathematical expressions,
    such as eval().

Input: s = "1 + 1"
Output: 2

Input: s = " 2-1 + 2 "
Output: 3

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:
    1 <= s.length <= 3 * 105
    s consists of digits, '+', '-', '(', ')', and ' '.
    s represents a valid expression.
    '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
    '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
    There will be no two consecutive operators in the input.
    Every number and running calculation will fit in a signed 32-bit integer.
"""


# 与第 241 题类似，同样使用了 运算二叉树 与 递归 。
def cal(s: str) -> int:
    # 如果表达式以 "-" 号开头（例如，"-(2 + 3)"），那么在前面添加一个 0
    if s.startswith("-"):
        s = "0" + s
    # 顺便考虑表达式以 "+" 开头的情况（虽然题目说了不可以）
    if s.startswith("+"):
        s = s[1:]

    # 如果公式内含有括号，则先计算所有括号的运算结果。
    # （例如，将 "1+(2+3)-(4-5)" 变为 "1+5--1"）
    while ")" in s:
        j = s.rfind(")")
        count = 1
        i = j - 1
        while i >= 0:
            if s[i] == ")":
                count += 1
            if s[i] == "(":
                count -= 1
                if count == 0:
                    break
            i -= 1
        temp = str(cal(s[i+1:j]))
        s = s[:i] + temp + s[j+1:]

    # 常规计算
    s = s.replace("--", "+")
    s = s.replace("-", "+-")
    s = s.replace("++", "+")
    array = s.split("+")
    for k in range(len(array)):
        if array[k] == "":
            array[k] = 0
        else:
            array[k] = int(array[k])
    return sum(array)


def calculate(s: str) -> int:
    # 首先去除空格
    s = s.replace(" ", "")

    return cal(s)


print(calculate("(((1+(4+5+2)-3)+(6+8)))+4"))
print(calculate("1+  1"))
print(calculate(" 2-1 + 2 "))
print(calculate("- (3 + (4 + 5))"))
print(calculate("(5-(1+(5)))"))
