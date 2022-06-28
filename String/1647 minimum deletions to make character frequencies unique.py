"""
https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/

A string s is called good
if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string.
For example, in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.

Input: s = "aab"
Output: 0
Explanation: s is already good.

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
"""


# solution：单调栈
def solution(s: str):
    # 先统计
    # {a: string.count(a) for a in set(string)}
    temp = [s.count(a) for a in set(s)]
    temp.sort()
    # 开始使用单调栈
    monotonic_stack = list()
    length = len(temp)
    ans = 0
    for i in range(length):
        if not monotonic_stack or monotonic_stack[-1] < temp[i]:
            monotonic_stack.append(temp[i])
        else:
            monotonic_stack.append(temp[i])
            k = len(monotonic_stack) - 1
            while k > 0:
                if monotonic_stack[k] == 0:
                    break
                if monotonic_stack[k] == monotonic_stack[k-1]:
                    monotonic_stack[k-1] -= 1
                    ans += 1
                else:
                    break
                k -= 1
    # print(monotonic_stack)
    return ans


print(solution("aab"))
print(solution("aaabbbcc"))
print(solution("ceabaacb"))
