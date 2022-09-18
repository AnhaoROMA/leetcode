"""
https://leetcode.com/problems/minimum-cost-for-tickets/

You have planned some train traveling one year in advance.
The days of the year in which you will travel are given as an integer array days.
Each day is an integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example,
    if we get a 7-day pass on day 2,
    then we can travel for 7 days: 2, 3, 4, 5, 6, 7, and 8.
Return the minimum number of dollars you need to travel every day in the given list of days.
"""


def min_cost(days: list[int], costs: list[int]) -> int:
    # """
    # 贪心算法：怎么购买周卡、月卡比较划算？
    # """
    # day_pay = costs[0]
    # week_pay = costs[1]
    # month_pay = costs[2]
    # # week_day := 购买周卡后，至少用几次才划算？
    # week_day = week_pay // day_pay + 1
    # # month_day := 购买月卡后，至少用几次才划算？
    # month_day = month_pay // day_pay + 1
    #
    # ans = 0
    #
    # length = len(days)
    # i = 0
    # while i < length:
    #     # 在第 i 天判断此时购买月卡是否划算。
    #     j = i + 1
    #     while j < length:
    #         if days[j] - days[i] >= 30:
    #             break
    #         j += 1
    #     if j - i >= month_day:
    #         i = j
    #         ans += month_pay
    #         continue
    #
    #     # 在第 i 天判断此时购买周卡是否划算。
    #     j = i + 1
    #     while j < length:
    #         if days[j] - days[i] >= 7:
    #             break
    #         j += 1
    #     if j - i >= week_day:
    #         i = j
    #         ans += week_pay
    #         continue
    #
    #     # 如果在第 i 天时购买月卡不合算、购买周卡也不合算，则当天就日付。
    #     ans += day_pay
    #     i += 1
    #
    # return ans

    """
    上面的思路是错的：
    [1,4,6,9,10,11,12,13,14,15,16,17,18,20,21,22,23,27,28]
    [3,13,45]

    改用动态规划求解。
    使用一个 dp 数组，其中 dp[i] 代表着我们旅行到 i 天为止需要的最少旅行价格。
    那么，
    如果当天不需要旅行（不在days中），当然这一天就不用额外买票，所以需要花费的价格等于昨天的价格；
    如果当前天需要旅行的话，那么需要求三种买票方式的最小价格：
        昨天的最少价格+一天的票 costs[0]，
        7天前的最少价格+7天的票钱 costs[1]，
        30天前的最少价格+30天的票钱 costs[2]。

    总之，递推公式是：
    dp[i] = dp[i-1]，当第i天不用旅行；
    dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])，当第i天需要旅行。
    """
    last_day = days[-1]
    dp = [0 for _ in range(last_day+1)]
    for i in range(1, last_day+1):
        if i not in days:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + costs[0]
            if i > 6:
                dp[i] = min(dp[i], dp[i-7] + costs[1])
            else:
                dp[i] = min(dp[i], costs[1])
            if i > 29:
                dp[i] = min(dp[i], dp[i-30] + costs[2])
            else:
                dp[i] = min(dp[i], costs[2])
    return dp[last_day]


# print(
#     min_cost(
#         days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15]
#     )
# )
# print(
#     min_cost(
#         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]
#     )
# )
print(
    min_cost(
        days=[1, 4, 6, 7, 8, 20], costs=[7, 2, 15]
    )
)
