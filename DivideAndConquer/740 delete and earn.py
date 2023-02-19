"""
https://leetcode.com/problems/delete-and-earn/

You are given an integer array nums.
You want to maximize the number of points you get by performing the following operation any number of times:
    Pick any nums[i] and delete it to earn nums[i] points.
    Afterwards, you must delete every element equal to nums[i]-1 and every element equal to nums[i]+1.

Return the maximum number of points you can earn by applying the above operation some number of times.

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
    - Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
    - Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
    - Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
    - Delete a 3 again to earn 3 points. nums = [3].
    - Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.

Constraints:
    1 <= nums.length <= 2 * 10^4
    1 <= nums[i] <= 10^4
"""

from collections import Counter


def deleteAndEarn(nums: list[int]) -> int:
    """
    如果
        nums = [1, 2, 3, 5, 6, 7, 9, 10]
    那么
        deleteAndEarn(nums) = deleteAndEarn([1, 2, 3]) + deleteAndEarn(5, 6, 7]) + deleteAndEarn([9, 10])

    也就是说，可以用分治法的思想去解题。

    对于每一个分治的内容，应该使用动态规划的算法求解。
    """

    counts = dict(Counter(nums))
    keys = sorted(list(counts.keys()))
    length = len(keys)
    memory = {}

    def helping_hand(x: list[int]) -> int:
        # # 一开始我以为要么取奇数序列、要么取偶数序列，
        # # 但是后来发现是不对的。
        # size = len(x)
        # odd_result = 0
        # for k in range(1, size, 2):
        #     odd_result += x[k]*counts[x[k]]
        # even_result = 0
        # for k in range(0, size, 2):
        #     even_result += x[k]*counts[x[k]]
        # return max(odd_result, even_result)
        if not x:
            return 0
        elif x[0] in memory:
            return memory[x[0]]
        elif len(x) == 1:
            memory[x[0]] = x[0]*counts[x[0]]
            return memory[x[0]]
        else:
            memory[x[0]] = max(x[0]*counts[x[0]]+helping_hand(x[2:]), x[1]*counts[x[1]]+helping_hand(x[3:]))
            return memory[x[0]]

    ans = 0
    i = 0
    j = i + 1
    while j < length:
        if keys[j]-keys[j-1] > 1:
            ans += helping_hand(keys[i:j])
            i = j
            j = i + 1
        else:
            j += 1
    ans += helping_hand(keys[i:j])
    return ans


print(deleteAndEarn([2, 2, 3, 3, 3, 4, 7, 7, 8]))
print(deleteAndEarn([1, 2, 3, 5, 6, 7, 9, 10]))
