"""
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Constraints:
    3 <= nums.length <= 3000
    -10^5 <= nums[i] <= 10^5
"""

#
# 假如题目为：
# 有一个数组，数组内的元素代表点的坐标。请从中找出所有的等腰三角形。
#
# 解法为：先找顶点。
# 复杂度为 O(n^2)
#


def threeSum(nums: list[int]):
    #
    # 之前我们做过 twoSum ，那可以参考上面的“等腰三角形”问题，写出复杂度为 n^2 的解法。
    #
    nums.sort()
    result = set()
    sum = 0
    length = len(nums)
    for i in range(length):
        target = sum - nums[i]
        visited = set()
        for j in range(i+1, length):
            if target-nums[j] in visited:
                result.add((nums[i], target-nums[j], nums[j]))
            else:
                visited.add(nums[j])
    return result


print(threeSum([-1, 0, 1, 2, -1, -4]))
