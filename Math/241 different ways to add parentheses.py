"""
https://leetcode.com/problems/different-ways-to-add-parentheses/

Given a string expression of numbers and operators,
return all possible results from computing all the different possible ways
to group numbers and operators.
You may return the answer in any order.

The test cases are generated such that the output values fit in a 32-bit integer
and the number of different results does not exceed 10^4.

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Constraints:
    1 <= expression.length <= 20
    expression consists of digits and the operator '+', '-', and '*'.
    All the integer values in the input expression are in the range [0, 99].
"""


def cal(expression: str) -> list[int]:
    """
        思路：运算二叉树。
            +
           / \
          /   \
        (3)   (4)
    """
    ans = list()
    # 记录式中所有运算符的位置
    operators_index = list()
    length = len(expression)
    for i in range(length):
        if expression[i] in {"+", "-", "*"}:
            operators_index.append(i)
    # 如果式中不存在运算符
    # 说明表达式只有一个数字，直接返回即可
    if not operators_index:
        ans.append(int(expression))
        return ans
    # 如果式中存在运算符
    # 寻找每一种 运算二叉树的根节点 的可能
    for operator_index in operators_index:
        operator = expression[operator_index]
        left_expression = expression[:operator_index]
        right_expression = expression[operator_index+1:]
        # print(":::::::::::::")
        # print(left_expression)
        # print(operator)
        # print(right_expression)
        # print(":::::::::::::")
        if operator == "+":
            # 分别求出左、右式的运算结果（所有可能）
            left_result = cal(left_expression)
            right_result = cal(right_expression)
            for i in left_result:
                for j in right_result:
                    ans.append(i+j)
        if operator == "-":
            # 分别求出左、右式的运算结果（所有可能）
            left_result = cal(left_expression)
            right_result = cal(right_expression)
            for i in left_result:
                for j in right_result:
                    ans.append(i-j)
        if operator == "*":
            # 分别求出左、右式的运算结果（所有可能）
            left_result = cal(left_expression)
            right_result = cal(right_expression)
            for i in left_result:
                for j in right_result:
                    ans.append(i*j)
    return ans


print(cal("2*3-4*5"))
print(cal("2-1-1"))
