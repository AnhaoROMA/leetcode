"""
https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
"""


def minCost(colors: str, neededTime: list[int]) -> int:
    """
    动态规划
    """
    n = len(neededTime)
    if n == 1:
        return 0
    """
    dp[i] := 前面 i-1 个气球已经安置妥当了（指代价最小地使前面已经色彩缤纷），接着处理第 i 个气球
    
    if colors[i] == last_color:
        dp[i] = min(neededTime[i], <同颜色带中最大的>) + dp[i-1]
    else:
        dp[i] = dp[i-1]
    """
    dp = list()
    dp.append(0)
    if colors[1] == colors[0]:
        cur_max = max(neededTime[1], neededTime[0])
        last_color = colors[1]
        dp.append(min(neededTime[1], neededTime[0]))
    else:
        cur_max = neededTime[1]
        last_color = colors[1]
        dp.append(0)
    for i in range(2, n):
        if colors[i] == last_color:
            if cur_max < neededTime[i]:
                dp.append(dp[i-1]+cur_max)
                cur_max = neededTime[i]
            else:
                dp.append(dp[i-1]+neededTime[i])
        else:
            dp.append(dp[-1])
            cur_max = neededTime[i]
            last_color = colors[i]
    return dp[-1]


print(minCost("abaac", [1,2,3,4,5]))
print(minCost("abc", [1,2,3]))
print(minCost("aabaa", [1,2,3,4,1]))
print(minCost("bbbaaa", [4,9,3,8,8,9]))
