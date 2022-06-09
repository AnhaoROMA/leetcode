"""
https://leetcode.com/problems/minimum-window-substring/

Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s
such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.
"""


#
# solution:
# 用双指针 left 和 right 表示一个窗口。
#     1、right 向右移增大窗口，直到窗口包含了所有要求的字母。进行第 2 步。
#     2、记录此时的长度，left 向右移动，开始减少长度，每减少一次，就更新最小长度。
#        直到当前窗口不包含所有字母，回到第 1 步。
#
def judge(s_set, t_set) -> bool:
    """
    判断：
        t_set in s_set
    """
    for element in t_set:
        if element not in s_set:
            return False
        if s_set[element] < t_set[element]:
            return False
    return True


def window(s: str, t: str) -> str:
    if len(s) < len(t):
        return ""

    # t_set 表示 t 中每个字符出现的次数
    t_set = dict()
    for c in t:
        if c not in t_set:
            t_set[c] = 1
        else:
            t_set[c] += 1
    # print(t_set)

    length = len(s)
    result = ""

    left = 0
    right = 0
    s_set = dict()  # s_set 表示 s[left : right+1] 中每个字符出现的次数
    while right < length:
        if s[right] not in s_set:
            s_set[s[right]] = 1
        else:
            s_set[s[right]] += 1

        while judge(s_set, t_set):
            # print(s[left:right+1]) 先打印出来看看符合条件的子序列
            if len(result) == 0:
                result = s[left:right+1]
            else:
                if (right - left + 1) < len(result):
                    result = s[left:right + 1]
            s_set[s[left]] -= 1
            left += 1

        right += 1

    return result


print(window("ADOBECODEBANC", "ABC"))
print(window("a", "b"))
