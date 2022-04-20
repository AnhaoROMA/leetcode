"""
https://leetcode.com/problems/palindrome-number/

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""

# 解题思路：https://www.code-recipe.com/post/palindrome-number


def is_palindrome(x: int) -> bool:
    # If x is a negative number it is not a palindrome
    # If x % 10 = 0, in order for it to be a palindrome the first digit should also be 0
    if x < 0:
        return False
    if x > 0 and x % 10 == 0:
        return False

    reversed_num = 0
    while x > reversed_num:
        reversed_num = reversed_num * 10 + x % 10
        x = x // 10

    # If x is equal to reversed number then it is a palindrome
    # If x has odd number of digits, dicard the middle digit before comparing with x
    # Example, if x = 23132, at the end of for loop x = 23 and reversedNum = 231
    # So, reversedNum/10 = 23, which is equal to x
    return True if (x == reversed_num or x == reversed_num // 10) else False
