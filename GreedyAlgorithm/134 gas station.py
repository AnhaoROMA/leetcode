"""
https://leetcode.com/problems/gas-station/

There are n gas stations along a circular route,
where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank
and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index
if you can travel around the circuit once in the clockwise direction,
otherwise return -1.

If there exists a solution, it is guaranteed to be unique.
"""


def gas_station(gas: list[int], cost: list[int]) -> int:
    # """
    # 常规的思考是逐个判断。
    #
    # 然后果不其然 TLE 了。（ 34 / 37 ）
    # """
    # length = len(gas)
    # for i in range(length):
    #     if gas[i] < cost[i]:
    #         continue
    #     remain = gas[i] - cost[i]
    #     j = i + 1
    #     j = j % length
    #     while j != i:
    #         remain = remain + gas[j] - cost[j]
    #         if remain < 0:
    #             break
    #         j += 1
    #         j = j % length
    #     if j == i:
    #         return i
    # return -1

    """
    上面的常规思考的时间复杂度是 O(n^2)，
    现在去考虑如何减少判断的数量（就是不要“逐个”判断）。
    """
    length = len(gas)
    # 如何减少判断的数量呢？
    # 如果从 i 刚好不能抵达 j （i.e.从 i 能抵达 j-1 却不能抵达 j），
    # 那么对于任意 k \in [i, j)，
    # 从 k 出发都不可能抵达 j 。
    # 为什么呢？
    #
    # 由前提，
    # 对于任意 k \in [i, j)，
    # 从 i 出发、到达 k 时，车内的余油一定是大于等于零的，
    # 那如果直接从 k 出发的话，（此时是没有任何余油的），基础更差，是不可能到达 j 的！
    i = 0
    while i < length:
        if gas[i] < cost[i]:
            i += 1
            continue
        remain = gas[i] - cost[i]
        j = i + 1
        j = j % length
        while j != i and remain >= 0:
            remain = remain + gas[j] - cost[j]
            j += 1
            j = j % length
        if remain < 0 and j == i:
            break
        elif remain < 0:
            if j < i:
                break
            i = j
            continue
        else:
            return i
    return -1


print(
    gas_station(
        [4, 5, 2, 6, 5, 3],
        [3, 2, 7, 3, 2, 9]
    )
)
print(
    gas_station(
        [1, 2, 3, 4, 3, 2, 4, 1, 5, 3, 2, 4],
        [1, 1, 1, 3, 2, 4, 3, 6, 7, 4, 3, 1]
    )
)
print(
    gas_station(
        [1, 2, 3, 4, 5],
        [3, 4, 5, 1, 2]
    )
)
print(
    gas_station(
        [2, 3, 4],
        [3, 4, 3]
    )
)
