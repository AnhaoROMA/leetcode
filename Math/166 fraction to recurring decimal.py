"""
https://leetcode.com/problems/fraction-to-recurring-decimal/

Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 10^4 for all the given inputs.

Input: numerator = 1, denominator = 2
Output: "0.5"

Input: numerator = 2, denominator = 1
Output: "2"

Input: numerator = 4, denominator = 333
Output: "0.(012)"

Constraints:
    -2^{31} <= numerator, denominator <= 2^{31} - 1
    denominator != 0
"""


def fractionToDecimal(numerator: int, denominator: int) -> str:
    # 先解决符号问题
    if numerator * denominator < 0:
        numerator = abs(numerator)
        denominator = abs(denominator)
        ans = "-"
    else:
        numerator = abs(numerator)
        denominator = abs(denominator)
        ans = ""
    # 算整数部分
    ans += str(numerator//denominator)
    numerator = numerator % denominator
    # 添加小数点
    if numerator == 0:
        return ans
    ans += "."
    # 算小数部分
    a = []  # a[] := 余数
    b = []  # b[] := 商

    while numerator not in a:
        a.append(numerator)
        temp = ""
        numerator *= 10  # numerator 一定小于 denominator ！
        temp = str(numerator//denominator)
        numerator = numerator % denominator
        b.append(temp)

        # 如果能除尽
        if numerator == 0:
            break

    if numerator == 0:
        # 如果是由于除尽了而停止
        ans += "".join(b)
    else:
        # 如果是因为发现了循环而停止
        index = a.index(numerator)
        ans += "".join(b[:index])
        ans += "("
        ans += "".join(b[index:])
        ans += ")"
    return ans


print(fractionToDecimal(numerator=4, denominator=333))
print(fractionToDecimal(numerator=665, denominator=33))
print(fractionToDecimal(numerator=-50, denominator=8))
