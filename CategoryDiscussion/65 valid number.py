"""
https://leetcode.com/problems/valid-number/

A valid number can be split up into these components (in order):
    A decimal number or an integer.
    (Optional) An 'e' or 'E', followed by an integer.

A decimal number can be split up into these components (in order):
    (Optional) A sign character (either '+' or '-').
    One of the following formats:
        One or more digits, followed by a dot '.'.
        One or more digits, followed by a dot '.', followed by one or more digits.
        A dot '.', followed by one or more digits.

An integer can be split up into these components (in order):
    (Optional) A sign character (either '+' or '-').
    One or more digits.

For example, all the following are valid numbers:
[
    "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10",
    "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"
],
while the following are not valid numbers:
[
    "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"
].

Given a string s, return true if s is a valid number.

Input: s = "0"
Output: true

Input: s = "e"
Output: false

Input: s = "."
Output: false
"""
digits_set = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]
digits_set = set(digits_set)


def valid_integer(s: str) -> bool:
    if len(s) == 0:
        return False
    if s[0] == "+":
        unsigned_part = s[1:]
        if len(unsigned_part) == 0:
            return False
    elif s[0] == "-":
        unsigned_part = s[1:]
        if len(unsigned_part) == 0:
            return False
    else:
        unsigned_part = s

    for digit in unsigned_part:
        if digit not in digits_set:
            return False
    return True


def valid_decimal(s: str) -> bool:
    if len(s) == 0:
        return False

    if "." not in s:
        return valid_integer(s)

    if s[0] == "+":
        unsigned_part = s[1:]
        if len(unsigned_part) == 0:
            return False
    elif s[0] == "-":
        unsigned_part = s[1:]
        if len(unsigned_part) == 0:
            return False
    else:
        unsigned_part = s

    if "+" in unsigned_part or "-" in unsigned_part:
        return False
    dot_index = unsigned_part.index(".")
    left = unsigned_part[:dot_index]
    right = unsigned_part[dot_index+1:]
    if len(left) == 0 and len(right) == 0:
        return False
    return (len(left) == 0 or valid_integer(left)) and \
           (len(right) == 0 or valid_integer(right))


def valid_number(s: str) -> bool:
    if "e" in s:
        e_index = s.index("e")
        left = s[:e_index]
        right = s[e_index+1:]
        return (valid_integer(left) or valid_decimal(left)) and valid_integer(right)
    elif "E" in s:
        e_index = s.index("E")
        left = s[:e_index]
        right = s[e_index + 1:]
        return (valid_integer(left) or valid_decimal(left)) and valid_integer(right)
    else:
        return valid_integer(s) or valid_decimal(s)


a = "0089"
print(valid_number(a))
b = "-0.1"
print(valid_number(b))
c = "+3.14"
print(valid_number(c))
d = "4."
print(valid_number(d))
e = "-.9"
print(valid_number(e))
f = "2e10"
print(valid_number(f))
g = "-90E3"
print(valid_number(g))
h = "3e+7"
print(valid_number(h))
i = "+6e-1"
print(valid_number(i))
j = "53.5e93"
print(valid_number(j))
k = "-123.456e789"
print(valid_number(k))
print("= = = = = = = = = = = = = =")
m = "1a"
print(valid_number(m))
n = "1e"
print(valid_number(n))
o = "e3"
print(valid_number(o))
p = "99e2.5"
print(valid_number(p))
q = "--6"
print(valid_number(q))
r = "-+3"
print(valid_number(r))
u = "95a54e53"
print(valid_number(u))
t = "abc"
print(valid_number(t))
