"""
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

A conveyor belt has packages that must be shipped from one port to another within days days.

The i-th package on the conveyor belt has a weight of weights[i].
Each day, we load the ship with packages on the conveyor belt (in the order given by weights).
We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship
    that will result in all the packages on the conveyor belt being shipped within days days.

Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given,
so using a ship of capacity 14 and splitting the packages into parts
    like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10)
is not allowed.

Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4

Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1

Constraints:
    1 <= days <= weights.length <= 5 * 10^4
    1 <= weights[i] <= 500
"""


def shipWithinDays(weights: list[int], days: int) -> int:
    """
    这一题一看数据规模就知道要用二分查找。

    船的容积 C 的可能可行解的区间在 [ max(weights), sum(weights) ]。
    """

    number_of_packages = len(weights)

    def if_possible(capacity: int) -> bool:
        p = 0
        d = 0
        while d < days:
            temp = 0
            while p < number_of_packages:
                if temp+weights[p] > capacity:
                    break
                else:
                    temp += weights[p]
                    p += 1
            if p >= number_of_packages:
                return True
            d += 1
        return False

    i = max(weights)
    j = sum(weights)
    while i < j:
        k = (i + j) // 2
        if if_possible(capacity=k) is True:
            j = k
        else:
            i = k + 1
    return j


print(shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
print(shipWithinDays([1, 1, 1, 1, 100], 2))
print(shipWithinDays([1, 1, 1, 1, 100], 4))
print(shipWithinDays([1, 1, 1, 1, 100], 1))
print(shipWithinDays([3, 2, 2, 4, 1, 4], 3))
