"""
https://leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p),
implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
"""

"""
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
"""


def whether_matching(s: str, p: str) -> bool:
    len_s = len(s)
    len_p = len(p)
    hashmap = [[False for _ in range(len_p + 1)] for _ in range(len_s + 1)]
    hashmap[0][0] = True
    for j in range(0, len_p):
        if p[j] != "*":
            hashmap[0][j+1] = False
        else:
            # p[j] == "*"
            hashmap[0][j+1] = hashmap[0][j]

    for i in range(len_s):
        for j in range(len_p):
            if p[j] == "*":
                if j == 0:
                    hashmap[i+1][j+1] = True
                else:
                    # j > 0
                    temp = list()
                    tmp = hashmap[0:i+1]
                    for t in tmp:
                        temp.append(t[j])

                    if (hashmap[i+1][j] is True) or (True in temp):
                        hashmap[i+1][j+1] = True
                    else:
                        hashmap[i+1][j+1] = False
            elif p[j] == "?":
                hashmap[i+1][j+1] = hashmap[i][j]
            else:
                hashmap[i+1][j+1] = hashmap[i][j] and s[i] == p[j]
    return hashmap[-1][-1]


string = "abbbbbaabbababaabaabbbbababbbabbbaaaaaabaaaaaaabaabbaaabababbbaabaabbabbabbaabaaabaababbbbbaababaabbaaaabbbbabaaaaababababbabbabbbabbababaabbaabaaaaabbaaabbbbaaaabbaabbbbbabbabbabbbaaaabbbaabaaabbbaaaa"

pattern = "ba**a*a*a****a***ba**aa*b***a*ab**a**a***a**bbb***bb*baab**ba***b*ba****abbb**abab******abaa***abaaa***"
print(whether_matching(s=string, p=pattern))
