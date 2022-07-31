"""
https://leetcode.com/problems/add-strings/

Given two non-negative integers,
num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library
    for handling large integers (such as BigInteger).
You must also not convert the inputs to integers directly.

Input: num1 = "11", num2 = "123"
Output: "134"

Input: num1 = "456", num2 = "77"
Output: "533"

Input: num1 = "0", num2 = "0"
Output: "0"
"""


def add_strings(num1: str, num2: str) -> str:
    ans = ""
    if_carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    while i >= 0 or j >= 0 or if_carry != 0:
        if i < 0:
            val_1 = 0
        else:
            val_1 = int(num1[i])
        if j < 0:
            val_2 = 0
        else:
            val_2 = int(num2[j])
        tmp = val_1 + val_2 + if_carry
        ans = str(tmp % 10) + ans
        if_carry = tmp // 10
        i -= 1
        j -= 1
    return ans


print(add_strings("456", "77"))
print(add_strings("11", "123"))
