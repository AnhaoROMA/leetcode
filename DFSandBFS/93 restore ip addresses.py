"""
https://leetcode.com/problems/restore-ip-addresses/

A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.

Given a string s containing only digits,
return all possible valid IP addresses that can be formed by inserting dots into s.
You are not allowed to reorder or remove any digits in s.
You may return the valid IP addresses in any order.
"""
MAX_COUNT = 4


def restore_ip_addresses(string):
    result = list()
    length = len(string)
    stack = list()

    for i in range(3):
        if length - i - 1 > (MAX_COUNT - 1) * 3:
            continue
        if length - i - 1 < MAX_COUNT - 1:
            break
        if string[0] == "0":
            stack.append([[string[0]], string[1:], 1])
            break
        temp_value = int(string[0: i + 1])
        if temp_value > 255:
            break
        else:
            stack.append([[string[0: i + 1]], string[i + 1:], 1])
    # print(stack)
    while len(stack) != 0:
        element = stack.pop()
        tmp_result = element[0]
        sub_string = element[1]
        count = element[2]

        if count == MAX_COUNT:
            if len(sub_string) == 0:
                result.append(
                    tmp_result[0] + "." + tmp_result[1] + "." + tmp_result[2] + "." + tmp_result[3]
                )
            else:
                continue
        else:
            for i in range(3):
                if len(sub_string) - i - 1 > (MAX_COUNT - count - 1) * 3:
                    continue
                if len(sub_string) - i - 1 < MAX_COUNT - count - 1:
                    break
                if sub_string[0] == "0":
                    stack.append(
                        [
                            tmp_result + [sub_string[0: i + 1]],
                            sub_string[1:],
                            count + 1
                        ]
                    )
                    break
                temp_value = int(sub_string[0: i + 1])
                if temp_value > 255:
                    break
                else:
                    stack.append(
                        [
                            tmp_result + [sub_string[0: i + 1]],
                            sub_string[i + 1:],
                            count + 1
                        ]
                    )
    return result


s = "101023"
r = restore_ip_addresses(s)
print(r)
