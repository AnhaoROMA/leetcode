"""
https://leetcode.com/problems/regular-expression-matching/

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
"""


def re(s: str, p: str) -> bool:
    len_s = len(s)
    len_p = len(p)
    hashmap = [[False for _ in range(len_p + 1)] for _ in range(len_s + 1)]
    hashmap[0][0] = True
    for j in range(0, len_p):
        if p[j] == "*":
            if j == 0:
                hashmap[0][j+1] = False
            else:
                hashmap[0][j+1] = hashmap[0][j] or hashmap[0][j-1]
        else:
            hashmap[0][j+1] = False
    # print(hashmap)
    for i in range(len_s):
        for j in range(len_p):
            if p[j] == "*":
                if j == 0:
                    # "*"出现于字符串的开头
                    hashmap[i+1][j+1] = False
                else:
                    hashmap[i+1][j+1] = hashmap[i+1][j] or hashmap[i+1][j-1] or (hashmap[i][j+1] and (s[i] == p[j-1] or p[j-1] == "."))
            else:
                hashmap[i+1][j+1] = hashmap[i][j] and (s[i] == p[j] or p[j] == ".")
    # print(hashmap)
    return hashmap[-1][-1]


string = "aa"
pattern = "a*"
print(re(s=string, p=pattern))
