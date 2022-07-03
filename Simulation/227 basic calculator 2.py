"""
https://leetcode.com/problems/basic-calculator-ii/

Given a string s which represents an expression,
evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid.
All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function
which evaluates strings as mathematical expressions, such as eval().

Input: s = "3+2*2"
Output: 7

Input: s = " 3/2 "
Output: 1

Input: s = " 3+5 / 2 "
Output: 5

Constraints:
    1 <= s.length <= 3 * 105
    s consists of integers and operators ('+', '-', '*', '/')
        separated by some number of spaces.
    s represents a valid expression.
    All the integers in the expression are non-negative integers in the range [0, 2^31-1].
    The answer is guaranteed to fit in a 32-bit integer.
"""


def cal(s: str) -> int:
    # 先做乘除法运算
    i = 0
    while i < len(s):
        if s[i] in {"*", "/"}:
            m = i - 1
            while m >= 0:
                if s[m] not in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                    break
                m -= 1
            n = i + 1
            while n < len(s):
                if s[n] not in {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}:
                    break
                n += 1
            left = int(s[m+1:i])
            right = int(s[i+1:n])
            if s[i] == "*":
                tmp = left * right
            else:
                tmp = left // right
            s = s[:m+1] + str(tmp) + s[n:]
            i = m
        i += 1
    # 再做加减法
    s = s.replace("-", "+-")
    tmp = s.split("+")
    ans = 0
    for t in tmp:
        ans += int(t)
    return ans


def calculator(s: str) -> int:
    # 先去掉空格
    s = s.replace(" ", "")

    return cal(s)


print(calculator("3+2*2"))
