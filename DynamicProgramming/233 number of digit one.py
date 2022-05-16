"""
https://leetcode.com/problems/number-of-digit-one/

Given an integer n,
count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Input: n = 13
Output: 6
"""


def count(num: int) -> int:
    if num == 0:
        return 0
    result_list = [0]
    for n in range(10):
        if (10 ** n <= num) and (10 ** (n+1) > num):
            break
    # n = int(math.log(num, 10))
    # print(n)
    for i in range(n):
        result_list.append(sum(result_list) * 9 + 10 ** i)
    # print(result_list)
    past = sum(result_list)

    quotient = num // (10 ** n)
    remain = num % (10 ** n)

    if quotient == 1:
        return quotient * past + count(remain) + remain + 1
    else:
        return quotient * past + count(remain) + 10 ** n


a = 1001
print(count(a))
