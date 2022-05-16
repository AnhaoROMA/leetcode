"""
https://leetcode.com/problems/ugly-number/

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
"""


def ugly(num: int) -> bool:
    if num <= 0:
        return False
    elif num == 1:
        return True
    else:
        while num % 5 == 0:
            num /= 5
        while num % 3 == 0:
            num /= 3
        while num % 2 == 0:
            num /= 2

        if num == 1:
            return True
        else:
            return False
