"""
https://leetcode.com/problems/combination-sum-iii/

Find all valid combinations of k numbers that sum up to n
such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.

Return a list of all possible valid combinations.
The list must not contain the same combination twice,
and the combinations may be returned in any order.

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
"""


def dfs(temp_result, temp_k, temp_n):
    result = list()
    if len(temp_result) == 0:
        next_value = 1
    else:
        next_value = temp_result[-1] + 1
    if next_value > 9:
        return result
    for i in range(next_value, 10):
        result.append([temp_result+[i], temp_k - 1, temp_n - i])
    return result


def solution(k: int, n: int):
    result = list()
    stack = dfs([], k, n)
    # print(stack)
    while len(stack) != 0:
        temp = stack.pop()
        # print(temp)
        if temp[1] == 0 and temp[2] == 0:
            result.append(temp[0])
        else:
            stack += dfs(temp[0], temp[1], temp[2])
    return result


a = 9
b = 45
print(solution(k=a, n=b))
