"""
https://leetcode.com/problems/expression-add-operators/

Given a string num that contains only digits and an integer target,
return all possibilities to insert the binary operators '+', '-', and/or '*'
between the digits of num
so that the resultant expression evaluates to the target value.

Note that operands in the returned expressions should not contain leading zeros.

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]
Explanation: Both "1*2*3" and "1+2+3" evaluate to 6.

Input: num = "232", target = 8
Output: ["2*3+2","2+3*2"]
Explanation: Both "2*3+2" and "2+3*2" evaluate to 8.

Input: num = "3456237490", target = 9191
Output: []
Explanation: There are no expressions
    that can be created from "3456237490" to evaluate to 9191.

Constraints:
    1 <= num.length <= 10
    num consists of only digits.
    -2^{31} <= target <= 2^{31} - 1
"""


def add_operators(num: str, target: int) -> list[str]:
    result = list()
    length = len(num)
    bfs = list()

    for i in range(1, length + 1):
        if i > 9 and int(num) > 2 ** 31:
            break
        if num.startswith("0"):
            bfs.append(
                [
                    num[:1],
                    0,
                    1,
                    0
                ]
            )
            break
        bfs.append(
            [
                num[:i],
                int(num[:i]),
                i,
                int(num[:i])
            ]
        )

    while bfs:
        expr, val, pos, prev = bfs.pop()
        if pos == length:
            if val == target:
                result.append(expr)
        else:
            for i in range(pos + 1, length + 1):
                if num[pos] == "0" and i - pos > 1:
                    break
                curr = int(num[pos:i])
                # 加法
                bfs.append(
                    [
                        expr + "+" + str(curr),
                        val + curr,
                        i,
                        curr
                    ]
                )
                # 减法
                bfs.append(
                    [
                        expr + "-" + str(curr),
                        val - curr,
                        i,
                        -1 * curr
                    ]
                )
                # 乘法
                bfs.append(
                    [
                        expr + "*" + str(curr),
                        val - prev + prev * curr,
                        i,
                        prev * curr
                    ]
                )
    return result


print(add_operators("2032", 8))
print(add_operators("3456237490", 9191))
