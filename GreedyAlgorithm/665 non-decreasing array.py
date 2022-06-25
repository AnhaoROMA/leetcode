"""
https://leetcode.com/problems/non-decreasing-array/

Given an array nums with n integers,
your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based)
such that (0 <= i <= n - 2).

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.
"""


# solution: 参考第 300 题
def check(nums: list[int]) -> bool:
    length = len(nums)
    tmp = [
        nums[0]
    ]
    for i in range(1, length):
        d = nums[i]
        if d >= tmp[-1]:
            tmp.append(d)
        else:
            length_tmp = len(tmp)
            for j in range(length_tmp):
                if tmp[j] > d:
                    tmp[j] = d
                    break
    if length - len(tmp) <= 1:
        return True
    else:
        return False


print(check([4, 2, 3]))
print(check([3, 4, 2, 3]))
print(check([-1, 4, 2, 3]))
