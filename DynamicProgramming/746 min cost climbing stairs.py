"""
https://leetcode.com/problems/min-cost-climbing-stairs/

You are given an integer array cost
where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Input: cost = [10,15,20]
Output: 15

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6

Constraints:
    2 <= cost.length <= 1000
    0 <= cost[i] <= 999
"""


# 动态规划，需两个记忆数组
# dp[i]：选择第 i 个位置作为起始点（必定选中第 i 个元素）时最小的代价；
# res[i] := min(dp[i], dp[i+1])；
def solution(cost: list[int]) -> int:
    length = len(cost)

    dp = [-1 for _ in range(length)]
    dp[-1] = cost[-1]
    dp[-2] = cost[-2]
    i = length - 3
    while i >= 0:
        dp[i] = min(dp[i+1], dp[i+2]) + cost[i]
        i -= 1
    # print(dp)
    res = [-1 for _ in range(length-1)]
    i = length - 2
    while i >= 0:
        res[i] = min(dp[i], dp[i+1])
        i -= 1
    # print(res)
    return res[0]


print(solution([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(solution([10, 15, 20]))
