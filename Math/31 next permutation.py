"""
https://leetcode.com/problems/next-permutation/

Input: nums = [1,2,3]
Output: [1,3,2]

Input: nums = [3,2,1]
Output: [1,2,3]

Input: nums = [1,1,5]
Output: [1,5,1]
"""


def solution(nums: list[int]) -> None:
    length = len(nums)
    # 单调栈：单调递增
    stack = [nums[-1]]
    i = length - 2
    while i >= 0:
        if nums[i] >= stack[-1]:
            stack.append(nums[i])
        else:
            length_stack = len(stack)
            for j in range(length_stack):
                if stack[j] > nums[i]:
                    break
            tmp = nums[i]
            nums[i] = stack[j]
            stack[j] = tmp
            for j in range(length_stack):
                nums[i + j + 1] = stack[j]
            return
        i -= 1
    nums.reverse()


a = [3, 2, 1]
solution(a)
print(a)
