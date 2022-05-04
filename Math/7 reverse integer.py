import math

"""
https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

"""
Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21
"""


def reverse(x: int) -> int:
    border = 2**31
    if x == 0:
        return 0
    result = 0
    if x < 0:
        sign = -1
    else:
        sign = 1
    unsigned = sign * x
    max_e = int(math.log(unsigned, 10)) + 1
    e = max_e - 1
    while e >= 0:
        t = unsigned // (10**e)
        unsigned -= t * 10 ** e
        result += t * 10**(max_e-e-1)
        e -= 1
    result = result * sign
    if result < -1 * border or result > border - 1:
        result = 0
    return result


y = 120
print(reverse(x=y))
