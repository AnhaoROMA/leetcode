"""
https://leetcode.com/problems/allocate-mailboxes/

Given the array houses
where houses[i] is the location of the i-th house along a street
and an integer k,
allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.

The test cases are generated so that the answer fits in a 32-bit integer.
"""


def min_distance(houses: list[int], k: int) -> int:
    """
    动态规划 之 最佳分组。

    # DP 数组的定义
    dp[n][k] --> k mailboxes covering the first n houses
    # 状态转移方程
    见程序。
    """
    houses.sort()
    n = len(houses)
    dp = {}

    def helper(first_n_houses, k_mailboxes) -> int:
        if (first_n_houses, k_mailboxes) in dp:
            return dp[(first_n_houses, k_mailboxes)]
        if first_n_houses <= k_mailboxes:
            return 0
        if k_mailboxes == 1:
            where_to_set_the_mailbox = first_n_houses // 2
            res = 0
            for i in range(first_n_houses):
                res += abs(houses[i]-houses[where_to_set_the_mailbox])
            dp[(first_n_houses, k_mailboxes)] = res
            return dp[(first_n_houses, k_mailboxes)]

        # 看看这新添加的第 first_n_houses 个房子应该被分到哪一组。
        # 首先是考虑“自立门户”。
        res = helper(first_n_houses-1, k_mailboxes-1)
        # 然后是与之前的 j 所房子组成一组。
        f = 0
        for j in range(2, first_n_houses-k_mailboxes+2):
            f += houses[first_n_houses-(j+1)//2]-houses[first_n_houses-j]
            if f > res:
                break
            res = min(res, f+helper(first_n_houses-j, k_mailboxes-1))  # 注意这里
        dp[(first_n_houses, k_mailboxes)] = res
        return res

    return helper(n, k)


print(min_distance([1, 4, 8, 10, 20], 3))
print(min_distance([2, 3, 5, 12, 18], 2))
