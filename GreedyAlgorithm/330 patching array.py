"""
https://leetcode.com/problems/patching-array/

Given a sorted integer array nums and an integer n,
add/patch elements to the array such that
    any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.

Input:
    nums = [1,3], n = 6
Output:
    1
Explanation:
    Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
    Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
    Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
    So we only need 1 patch.

Input:
    nums = [1,5,10], n = 20
Output:
    2
Explanation:
    The two patches can be [2, 4].

Input:
    nums = [1,2,2], n = 5
Output:
    0

Constraints:
    1 <= nums.length <= 1000
    1 <= nums[i] <= 10^4
    nums is sorted in ascending order.
    1 <= n <= 2^{31}-1
"""


def minPatches(nums: list[int], n: int) -> int:
    """
    贪心算法

    如果不考虑 nums[] 的限制，单单考虑 “满足包揽 [1, n]” 这一条。
    用数学归纳法的思想，
        如果我们已经包揽了 [1, m]，则再给一个 m+1，便可以包揽 [1, 2m+1]，
                        更一般地，再给一个 k>m，便可以包揽 [1, m]U[k, k+m]。

    现在开始考虑 nums[] 的限制，注意 nums[] 是 sorted 的。

    假设当走到 nums[i] 时，已经覆盖了 [1, x]，则在引入 nums[i+1] 时，
    1. 若 nums[i+1] <= x+1 ，则覆盖范围变更为 [1, nums[i+1]+x]
    2. 若 nums[i+1] > x+1 ，则需要补充 x+1 这个数

    注意本题中添加一个新元素与修改已有元素的代价是相同的，所以我们只需要考虑“添加”的操作。
    """

    count = 0  # 操作的步骤数

    current_upper_bound = 0  # current_range = [0, current_upper_bound]
    i = 0  # 放在 nums[] 上的指针（相当于注释中的 i+1）
    length = len(nums)

    while current_upper_bound < n:
        if i == length:
            # 如果 nums[] 没有利用价值了（已经遍历到头了）
            count += 1  # 添加 current_upper_bound+1 这个数
            current_upper_bound = current_upper_bound + (current_upper_bound + 1)
        else:
            if nums[i] > current_upper_bound+1:
                count += 1  # 添加 current_upper_bound+1 这个数
                current_upper_bound = current_upper_bound + (current_upper_bound + 1)
            else:
                # tmp <= current_upper_bound
                current_upper_bound = current_upper_bound + nums[i]
                i += 1

    return count


print(minPatches([1,5,10], 20))
print(minPatches([1,3], 6))
print(minPatches([1,2,2], 5))
