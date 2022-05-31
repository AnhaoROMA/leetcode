"""
https://leetcode.com/problems/multiply-strings/

Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

"""
Input: num1 = "2", num2 = "3"
Output: "6"

Input: num1 = "123", num2 = "456"
Output: "56088"
"""

table = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9
}


def add(num1: str, num2: str) -> str:
    result = ""
    i = len(num1) - 1
    j = len(num2) - 1
    if_carry = 0
    while i >= 0 or j >= 0 or if_carry > 0:
        if i >= 0:
            val1 = table[num1[i]]
            i -= 1
        else:
            val1 = 0

        if j >= 0:
            val2 = table[num2[j]]
            j -= 1
        else:
            val2 = 0

        temp = val1 + val2 + if_carry
        if_carry = temp // 10
        result = str(temp % 10) + result
    return result


def add_a_list(a: list) -> str:
    length = len(a)
    if length == 0:
        return "0"
    elif length == 1:
        return a[0]
    else:
        tmp1 = a[0]
        for j in range(1, length):
            tmp2 = a[j]
            tmp1 = add(num1=tmp1, num2=tmp2)
    return tmp1


def multiply(num1: str, num2: str) -> str:
    result_list = list()

    j = len(num2) - 1
    while j >= 0:
        val2 = table[num2[j]]
        i = len(num1) - 1
        temp_result = ""
        if_carry = 0
        while i >= 0 or if_carry > 0:
            if i >= 0:
                val1 = table[num1[i]]
            else:
                val1 = 0
            temp = val1 * val2 + if_carry
            temp_result = str(temp % 10) + temp_result
            if_carry = temp // 10
            i -= 1

        for _ in range(len(num2)-j-1):
            temp_result += "0"
        while temp_result.startswith("0") and len(temp_result) > 1:
            temp_result = temp_result[1:]

        result_list.append(temp_result)
        j -= 1
        print(result_list)
    return add_a_list(result_list)


n1 = "0"
n2 = "52"
# print(add(num1=n1, num2=n2))
print(multiply(num1=n1, num2=n2))
