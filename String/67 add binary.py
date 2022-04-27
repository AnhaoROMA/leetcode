"""
https://leetcode.com/problems/add-binary/
"""


def add_binary(str1, str2):
    result = ""
    i = len(str1) - 1
    j = len(str2) - 1
    if_carry = 0
    while i >= 0 or j >= 0 or if_carry == 1:
        if i < 0:
            i_val = 0
        else:
            i_val = int(str1[i])
        if j < 0:
            j_val = 0
        else:
            j_val = int(str2[j])

        if_carry += i_val
        if_carry += j_val
        result = str(if_carry % 2) + result
        if_carry = if_carry // 2

        i -= 1
        j -= 1

    return result


a = "1010"
b = "1011"
print(add_binary(a, b))
