"""
https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Input: nums = [2,0,1]
Output: [0,1,2]
"""

# solution:
# 定义red指针指向开头位置，blue指针指向末尾位置。
# 从头开始遍历原数组，如果遇到0，则交换该值和 red 指针指向的值，并将 red 指针后移一位。
# 若遇到2，则交换该值和 blue 指针指向的值，并将 blue 指针前移一位。
# 若遇到1，则继续遍历。


def sort(colors: list[int]):
    length = len(colors)
    red = 0
    blue = length - 1
    pointer = 0
    while pointer <= blue:
        if colors[pointer] == 0:
            colors[red], colors[pointer] = colors[pointer], colors[red]
            red += 1
            pointer += 1
        elif colors[pointer] == 2:
            colors[blue], colors[pointer] = colors[pointer], colors[blue]
            blue -= 1
        else:
            # colors[pointer] == 1
            pointer += 1
    return colors


a = [2, 0, 2, 1, 1, 0]
b = [1, 2, 0]
print(sort(b))
