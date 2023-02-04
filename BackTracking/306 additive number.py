"""
https://leetcode.com/problems/additive-number/

An additive number is a string whose digits can form an additive sequence.

A valid additive sequence should contain at least three numbers.
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits, return true if it is an additive number or false otherwise.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Input: "112358"
Output: true
Explanation:
    The digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
    1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Input: "199100199"
Output: true
Explanation:
    The additive sequence is: 1, 99, 100, 199.
    1 + 99 = 100, 99 + 100 = 199

Constraints:
    1 <= num.length <= 35
    num consists only of digits.
"""


def isAdditiveNumber(num: str) -> bool:

    def is_redundant(number) -> bool:
        if number.startswith("0") and len(number) > 1:
            return False
        else:
            return True

    def is_able(before_1, before_2, after) -> bool:
        before = str(int(before_1) + int(before_2))
        if not after.startswith(before):
            return False
        else:
            length_before = len(before)
            if length_before == len(after):
                return True
            else:
                return is_able(before_2, before, after[length_before:])

    length = len(num)
    for i in range(length//2):
        for j in range(i+1, min((length+i)//2, length-i-2)+1):
            if is_redundant(num[:i+1]) is False or is_redundant(num[i+1:j+1]) is False:
                continue
            if is_able(num[:i+1], num[i+1:j+1], num[j+1:]) is True:
                return True
    return False


print(isAdditiveNumber("1023"))
print(isAdditiveNumber("211738"))
print(isAdditiveNumber("123"))
print(isAdditiveNumber("112358"))
print(isAdditiveNumber("199100199"))
