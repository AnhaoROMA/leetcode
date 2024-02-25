"""
https://leetcode.com/problems/largest-component-size-by-common-factor/

You are given an integer array of unique positive integers nums.
Consider the following graph:
    There are nums.length nodes, labeled nums[0] to nums[nums.length-1],
    There is an undirected edge between nums[i] and nums[j] if nums[i] and nums[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

Input: nums = [4,6,15,35]
Output: 4

Input: nums = [20,50,9,63]
Output: 2

Input: nums = [2,3,6,7,4,12,21,39]
Output: 8

Constraints:
    1 <= nums.length <= 2 * 10^4
    1 <= nums[i] <= 10^5
    All the values of nums are unique.
"""

import math


def largestComponentSize(nums: list[int]) -> int:

    def cal_primes(n: int) -> set[int]:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return cal_primes(n // i) | {i}
        return {n}

    """
    不断合并！
    """

    """
    但是这种做法会 TLE，正确的做法是：不是对 位置（index） 进行合并，而是对 约数（divisor） 进行合并。
    """

    components = dict()
    for num in nums:
        divisors = cal_primes(num)
        can_merge = list()
        for component in components:
            if components[component] & divisors:
                can_merge.append(component)
                divisors = divisors | components[component]
        new_key = "+".join(can_merge + [str(num)])
        components[new_key] = divisors
        for other in can_merge:
            del components[other]
        # print(components)

    res = 1
    for component in components:
        res = max(res, len(component.split("+")))
    return res


print(largestComponentSize([2,3,6,7,4,12,21,39]))
