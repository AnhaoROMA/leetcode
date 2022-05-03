"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.
"""

table = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}


def descartes_product(a, b):
    if a is None and b is None:
        return None
    if a is None:
        a = [""]
    if b is None:
        b = [""]
    result = list()
    for a_ in a:
        for b_ in b:
            result.append(a_+b_)
    return result


def letter_combinations(digits: str) -> list[str]:
    if len(digits) == 0:
        return []
    i = [""]
    for j in digits:
        t = table[j]
        i = descartes_product(a=i, b=t)
    return i


A = ["a"]
B = [""]
print(descartes_product(A, B))
print(letter_combinations(""))
