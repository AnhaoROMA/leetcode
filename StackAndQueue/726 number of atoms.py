"""
https://leetcode.com/problems/number-of-atoms/
"""


def countOfAtoms(formula: str) -> str:
    """"""
    """
        首先，简化问题
    """
    digits = {
        "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
    }
    lowercase = {
        "a", "b", "c", "d", "e", "f", "g",
        "h", "i", "j", "k", "l", "m", "n",
        "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z"
    }
    uppercase = {
        "A", "B", "C", "D", "E", "F", "G",
        "H", "I", "J", "K", "L", "M", "N",
        "O", "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z"
    }
    parts = list()
    length = len(formula)
    i = 0
    while i < length:
        if formula[i] in {"(", ")"}:
            parts.append(formula[i])
            i += 1
        elif formula[i] in digits:
            j = i + 1
            while j < length and formula[j] in digits:
                j += 1
            parts.append(int(formula[i:j]))
            i = j
        elif formula[i] in uppercase:
            j = i + 1
            while j < length and formula[j] in lowercase:
                j += 1
            parts.append(formula[i:j])
            i = j
        else:
            # invalid input
            i += 1
            return "error"
    # print(parts)

    """
        使用栈
    """
    cur = []
    stack = []
    length = len(parts)
    i = 0
    while i < length:
        if type(parts[i]) is int:
            temp, _ = cur.pop(-1)
            cur.append((temp, parts[i]))
        elif parts[i] == "(":
            stack.append(cur)
            cur = []
        elif parts[i] == ")":
            if i+1 < length and type(parts[i+1]) is int:
                for j in range(len(cur)):
                    cur[j] = (cur[j][0], cur[j][1]*parts[i+1])
                cur = stack.pop() + cur
                i += 1  # 如果 ")" 后面是一个数字，该数字在这个 if 中已经被处理了
        else:
            # element
            cur.append((parts[i], 1))
        i += 1
    # print(cur)
    # print(stack)
    while stack:
        cur += stack.pop()
    # print(cur)

    """
        整理答案
    """
    ans = dict()
    for element, number in cur:
        if element in ans:
            ans[element] += number
        else:
            ans[element] = number
    result = ""
    for element in sorted(ans.keys()):
        result += element
        if ans[element] > 1:
            result += str(ans[element])
    return result


print(countOfAtoms("(NaCl(CuCl2)3)2F"))
print(countOfAtoms("K4(ON(SO3)2)2"))
print(countOfAtoms("Mg(OH)2"))
print(countOfAtoms("Mg(OH)(Cl)"))
