"""
https://leetcode.com/problems/solve-the-equation/

Solve a given equation and return the value of 'x' in the form of a string "x=#value".
The equation contains only '+', '-' operation, the variable 'x' and its coefficient.
You should return "No solution" if there is no solution for the equation,
or "Infinite solutions" if there are infinite solutions for the equation.

If there is exactly one solution for the equation,
we ensure that the value of 'x' is an integer.

Input: equation = "x+5-3+x=6+x-2"
Output: "x=2"

Input: equation = "x=x"
Output: "Infinite solutions"

Input: equation = "2x=x"
Output: "x=0"

Constraints:
    3 <= equation.length <= 1000
    equation has exactly one '='.
    equation consists of integers with an absolute value in the range [0, 100]
    without any leading zeros, and the variable 'x'.
"""


def helping_hand(exp: str) -> [int, int]:
    x_num = 0
    n_num = 0

    length = len(exp)
    i = 0
    j = i
    while j < length:
        if exp[j] not in {"+", "-"}:
            j += 1
        else:
            part = exp[i:j]
            # print(part)
            if "x" in part:
                part = part[:-1]
                if part == "" or part == "+":
                    part = "1"
                elif part == "-":
                    part = "-1"
                else:
                    pass
                x_num += int(part)
            else:
                n_num += int(part)
            i = j
            j += 1
    # 最后一段
    part = exp[i:j]
    # print(part)
    if "x" in part:
        part = part[:-1]
        if part == "" or part == "+":
            part = "1"
        elif part == "-":
            part = "-1"
        else:
            pass
        x_num += int(part)
    else:
        n_num += int(part)
    return [x_num, n_num]


def solve(equation: str) -> str:
    [left, right] = equation.split("=")
    # 计算左式中 x 的系数与常数项系数。
    [x_left, n_left] = helping_hand(left)
    # 计算右式中 x 的系数与常数项系数。
    [x_right, n_right] = helping_hand(right)
    # 移项
    x_num = x_left - x_right
    n_num = n_right - n_left
    if x_num == 0:
        if n_num == 0:
            return "Infinite solutions"
        else:
            return "No solution"
    else:
        return "x="+str(n_num//x_num)


print(solve("x+5-3+x=6+x-2"))
