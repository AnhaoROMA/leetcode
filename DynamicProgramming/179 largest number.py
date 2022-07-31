"""
https://leetcode.com/problems/largest-number/

Given a list of non-negative integers nums,
arrange them such that they form the largest number and return it.

Since the result may be very large,
so you need to return a string instead of an integer.

Input: nums = [10,2]
Output: "210"

Input: nums = [3,30,34,5,9]
Output: "9534330"

Constraints:
    1 <= nums.length <= 100
    0 <= nums[i] <= 10^9
"""


def where_to_insert(array: list[str], string: str) -> int:
    length = len(array)
    for i in range(length):
        temp = array[i]
        if temp[0] > string[0]:
            """
            比如，
            向[..., "42", ...]中插入"33"，需再向后移动。
            """
            continue
        elif temp[0] < string[0]:
            """
            比如，
            向[..., "61", "42", ...]中插入"53"，需插在61和42之间。
            """
            return i
        else:
            """
            最困难的一种情况，
            例如，
            向[..., "34", "332", "31", ...]中插入"3"，此时应该插在哪里？
            向[..., "34", "332", "31", ...]中插入"32456"，此时应该插在哪里？
            """
            comparison_1 = temp + string
            comparison_2 = string + temp
            for j in range(len(comparison_1)):
                if comparison_1[j] > comparison_2[j]:
                    break
                elif comparison_1[j] < comparison_2[j]:
                    return i
                else:
                    continue
    return length


def largest_number(nums: list[int]) -> str:
    """
    遇到最值问题，DP是常用方法。
    """
    ans = list()
    length = len(nums)
    for i in range(length):
        nums[i] = str(nums[i])
    for i in range(length):
        tmp = nums[i]
        j = where_to_insert(ans, tmp)
        ans.insert(j, tmp)
    res = ""
    for c in ans:
        res += c
    while len(res) > 1 and res.startswith("0"):
        res = res[1:]
    return res


print(largest_number([3, 30, 34, 5, 9]))
print(largest_number([10, 2]))
print(largest_number([34323, 3432]))
