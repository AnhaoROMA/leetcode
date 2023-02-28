"""
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums,
find a subarray that has the largest product,
and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
    1 <= nums.length <= 2 * 10^4
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""


def maxProduct(nums: list[int]) -> int:
    """
    本题被归为 动态规划 类。

    对于数组中的每一个数，
        去求以它为结尾的 子数组的最小乘积（ min_product ） 与 子数组的最大乘积（ max_product ）。
    """
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if num > 0:
            max_product, min_product = max(num, max_product * num), min(num, min_product * num)
        elif num < 0:
            max_product, min_product = max(num, min_product * num), min(num, max_product * num)
        else:
            max_product = 0
            min_product = 0
        result = max(result, max_product)
    return result


print(maxProduct([-4, -3, -2]))
print(maxProduct([3, -1, 4]))
print(maxProduct([2, 3, -2, 4]))
print(maxProduct([-2, 0, -1]))
