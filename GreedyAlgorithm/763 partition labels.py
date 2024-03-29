"""
https://leetcode.com/problems/partition-labels/

You are given a string s.
We want to partition the string into as many parts as possible
    so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order,
the resultant string should be s.

Return a list of integers representing the size of these parts.

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Input: s = "eccbbbbdec"
Output: [10]

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
"""


def partition_labels(s: str) -> list[int]:
    length = len(s)
    ans = []
    i = 0
    while i < length:
        visited = set()
        visited.add(s[i])
        j = s.rfind(s[i])
        k = i+1
        while k < j+1:
            if s[k] in visited:
                k += 1
                continue
            visited.add(s[k])
            j = max(j, s.rfind(s[k]))
            k += 1
        ans.append(j-i+1)
        i = j + 1
    return ans


print(partition_labels("ababcbacadefegdehijhklij"))
print(partition_labels("eccbbbbdec"))
print(partition_labels("qiejxqfnqceocmy"))
