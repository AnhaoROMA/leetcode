"""
https://leetcode.com/problems/strange-printer/

There is a strange printer with the following two special properties:
    The printer can only print a sequence of the same character each time.
    At each turn,
        the printer can print new characters starting from and ending at any place
        and will cover the original existing characters.

Given a string s,
return the minimum number of turns the printer needed to print it.

Input: s = "aaabbb"
Output: 2
Explanation: Print "aaa" first and then print "bbb".

Input: s = "aba"
Output: 2
Explanation: Print "aaa" first and then print "b" from the second place of the string,
             which will cover the existing character 'a'.

Constraints:
    1 <= s.length <= 100
    s consists of lowercase English letters.
"""


def strange_printer(s: str) -> int:
    length = len(s)
    dp = [[-1 for _ in range(length)] for _ in range(length)]

    def cal(x: int, y: int) -> int:
        if dp[x][y] > -1:
            pass
        elif x > y:
            dp[x][y] = 0
        elif x == y:
            dp[x][y] = 1
        else:
            temp = 1 + cal(x, y-1)
            k = x
            while k < y:
                if s[k] == s[y]:
                    temp = min(
                        temp,
                        cal(x, k) + cal(k+1, y-1)
                    )
                k += 1
            dp[x][y] = temp
        return dp[x][y]

    return cal(0, length-1)


print(strange_printer("aaabbb"))
print(strange_printer("aba"))
print(strange_printer("abcba"))
print(strange_printer("caaabdbbcbccdbcbcdcccabdcdadbccaaaddaaccbadddabca"))
print(strange_printer("badcbcabd"))
