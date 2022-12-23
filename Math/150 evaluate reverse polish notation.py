"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
"""


def eval_rpn(tokens: list[str]) -> int:
    length = len(tokens)
    stack = list()
    i = 0
    while i < length:
        if tokens[i] == "+":
            num_2 = stack.pop()
            num_1 = stack.pop()
            stack.append(num_1+num_2)
        elif tokens[i] == "-":
            num_2 = stack.pop()
            num_1 = stack.pop()
            stack.append(num_1-num_2)
        elif tokens[i] == "*":
            num_2 = stack.pop()
            num_1 = stack.pop()
            stack.append(num_1*num_2)
        elif tokens[i] == "/":
            num_2 = stack.pop()
            num_1 = stack.pop()
            stack.append(int(num_1/num_2))
        else:
            stack.append(int(tokens[i]))
        i += 1
    return stack[0]


example_1 = ["2", "1", "+", "3", "*"]
example_2 = ["4", "13", "5", "/", "+"]
example_3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(
    eval_rpn(
        example_3
    )
)
