"""
https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

Given a string s and an integer k,
return the length of the longest substring of s
    such that the frequency of each character in this substring is greater than or equal to k.

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

Constraints:
    1 <= s.length <= 10^4
    s consists of only lowercase English letters.
    1 <= k <= 10^5
"""

from collections import Counter
import re


def longestSubstring(s: str, k: int) -> int:
    """
    对于字符串 s ，如果存在某个字符 char ，它的出现次数大于 0 且小于 k ，则任何包含 char 的子串都不可能满足要求。

    也就是说，我们将字符串按照 char 切分成若干段，则满足要求的最长子串一定出现在某个被切分的段内，而不能跨越一个或多个段。

    因此，可以考虑分治的方式求解本题。
    """
    statistics = Counter(s)
    split_symbols = []
    for char in statistics:
        if statistics[char] < k:
            split_symbols.append(char)
    if not split_symbols:
        return len(s)
    parts = re.split("|".join(split_symbols), s)
    return max([longestSubstring(part, k) for part in parts])


print(longestSubstring("weitong", 2))
print(longestSubstring("aaabb", 3))
print(longestSubstring("ababbc", 2))
