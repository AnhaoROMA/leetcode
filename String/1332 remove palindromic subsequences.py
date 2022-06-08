"""
https://leetcode.com/problems/remove-palindromic-subsequences/

You are given a string s consisting only of letters 'a' and 'b'.
In a single step you can remove one palindromic subsequence from s.

Return the minimum number of steps to make the given string empty.

A string is a subsequence of a given string
if it is generated by deleting some characters of a given string without changing its order.
Note that a subsequence does not necessarily need to be contiguous.

A string is called palindrome if is one that reads the same backward as well as forward.

Input: s = "ababa"
Output: 1
Explanation: s is already a palindrome,
             so its entirety can be removed in a single step.

Input: s = "abb"
Output: 2
Explanation: "abb" -> "bb" -> "".
Remove palindromic subsequence "a" then "bb".

Input: s = "baabb"
Output: 2
Explanation: "baabb" -> "b" -> "".
Remove palindromic subsequence "baab" then "b".

Constraints:
    1 <= s.length <= 1000
    s[i] is either 'a' or 'b'.
"""


#
# 这道题算是个脑筋急转弯。
# 注意题设给的是你可以删除任意一个回文子序列，也就是说你可以跳着找字母删除，
# 只要最后被删除的部分组合起来是个回文就行。
# 这道题由于又只有a和b两种字母，所以我们实际上最多只需要删除两次就可使得最后的字符串为空。
#
# 如果input字符串本身就是回文，删除一次
#
# 如果input字符串不是回文，那么我们首先把所有的a删除。
# 因为所有的相同字母组合起来一定是个回文串，所以只需要删除两次即可
# 答案只可能是0，1，2.
# 0:s为空，返回0.
# 1:s本身就是回文串。
# 2.其他情况
#
def solution(s: str) -> int:
    if not s:
        return 0
    if s == s[::-1]:
        return 1
    else:
        return 2
