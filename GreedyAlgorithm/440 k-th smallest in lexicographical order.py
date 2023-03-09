"""
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

Given two integers n and k,
return the k-th lexicographically smallest integer in the range [1, n].

Input: n = 13, k = 2
Output: 10
Explanation:
    The lexicographical order is
        [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9],
    so the second smallest number is 10.

Input: n = 1, k = 1
Output: 1

Constraints:
    1 <= k <= n <= 10^9
"""

import math


def findKthNumber(n: int, k: int) -> int:

    # ### 一步一步地走
    # temp = 1
    # count = 1
    # while count < k:
    #     if temp * 10 <= n:
    #         temp *= 10
    #     else:
    #         if temp + 1 <= n:
    #             temp += 1
    #             while temp % 10 == 0:
    #                 temp = temp // 10
    #         else:
    #             temp = temp // 10
    #             temp += 1
    #             while temp % 10 == 0:
    #                 temp = temp // 10
    #     count += 1
    # return temp

    ### 前缀树的思想

    # 子函数
    def get_num(prefix: int) -> int:
        """
        计算：在 [1, n] 中、以 prefix 为前缀的数有多少个。
        """
        a = str(n)
        b = str(prefix)
        a_size = len(a)
        b_size = len(b)
        c = a[:b_size]
        tmp11 = 0
        tmp10 = 1
        for _ in range(a_size-b_size):
            tmp10 *= 10
            tmp11 = 10 * tmp11 + 1
        if c < b:
            return tmp11
        elif c > b:
            return tmp11 + tmp10
        else:
            # c == b
            return tmp11 + n - prefix * tmp10 + 1

    # 主函数
    temp_prefix = 1
    while k > 1:
        count = get_num(prefix=temp_prefix)
        if k > count:
            k -= count
            temp_prefix += 1
        else:
            k -= 1
            temp_prefix *= 10
    return temp_prefix


print(findKthNumber(n=13, k=11))
print(findKthNumber(n=13, k=3))
print(findKthNumber(n=1, k=1))
print(findKthNumber(n=804289384, k=42641503))
