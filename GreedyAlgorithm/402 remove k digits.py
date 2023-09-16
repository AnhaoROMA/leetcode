"""
https://leetcode.com/problems/remove-k-digits/

Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.

Input:
    num = "1432219", k = 3
Output:
    "1219"
Explanation:
    Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Input:
    num = "10200", k = 1
Output:
    "200"
Explanation:
    Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Input:
    num = "10", k = 2
Output:
    "0"
Explanation:
    Remove all the digits from the number and it is left with nothing which is 0.

Constraints:
    1 <= k <= num.length <= 10^5
    num consists of only digits.
    num does not have any leading zeros except for the zero itself.
"""


def remove_k_digits(num: str, k: int) -> str:
    """
    贪心算法

    贪心策略：如果某一位比后一位大，则删掉该位。

    假设本题的 k 固定为 1，即只能删一个数字的前提下，能得到的最小的数字是什么？
    示例：
        比如 “143”，在看到 “4” 的时候，是没有删掉 “4” 的“欲望”的，但看到 “3” 的时候，就知道要删掉 “4” 了。
        （有点单调栈的想法在里面。）
        但如果数字是单调递增的，比如 "12345"，看到最后也没有想要删除的元素，所以就从后面开始删。

    而本题可以看作，连续执行上述操作 k 次。
    """

    if len(num) <= k:
        return "0"

    num += "!"  # as "!" < "[0, 1, ..., 9]"

    i = 0
    while k > 0:
        if num[i] > num[i+1]:
            num = num[:i] + num[i+1:]
            k -= 1
            if i > 0:
                i -= 1
        else:
            i += 1

    num = num[:-1]  # 去掉一开始的 "!"
    # 去掉开头的 "0"
    while num.startswith("0"):
        num = num[1:]
    if num == "":
        return "0"
    else:
        return num


print(remove_k_digits("1234567890", 9))
print(remove_k_digits("10001", 4))
print(remove_k_digits("112", 1))
print(remove_k_digits("1432219", 3))
print(remove_k_digits("10200", 1))
print(remove_k_digits("10", 2))
