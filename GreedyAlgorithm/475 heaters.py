"""
Winter is coming!

During the winter,
your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range.

Given the positions of houses and heaters on a horizontal line,
return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.

==========================================================================================

Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation:
    The only heater was placed in the position 2,
    and if we use the radius 1 standard, then all the houses can be warmed.

Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation:
    The two heater was placed in the position 1 and 4.
    We need to use radius 1 standard, then all the houses can be warmed.

Input: houses = [1,5], heaters = [2]
Output: 3

Constraints:
    1 <= houses.length, heaters.length <= 3 * 10^4
    1 <= houses[i], heaters[i] <= 10^9
"""


def findRadius(houses: list[int], heaters: list[int]) -> int:
    """
    贪心算法 { 二分查找 }
    """
    houses.sort()
    heaters.sort()

    length_heaters = len(heaters)

    def helping_hand(pos: int) -> int:
        if pos <= heaters[0]:
            return heaters[0]-pos
        if pos >= heaters[-1]:
            return pos-heaters[-1]
        m = 0
        n = length_heaters - 1
        while m+1 < n:
            k = (m+n)//2
            if pos > heaters[k]:
                m = k
            elif pos < heaters[k]:
                n = k
            else:
                return 0
        return min(pos-heaters[m], heaters[m+1]-pos)

    result = [0 for _ in range(len(houses))]
    for i in range(len(houses)):
        result[i] = helping_hand(houses[i])
    return max(result)


print(findRadius([1, 2, 3], [2]))
print(findRadius([1, 2, 3, 4], [1, 4]))
print(findRadius([1, 5], [2]))
print(
    findRadius(
        [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],
        [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
    )
)
print(
    findRadius(
        [25921153,510616708],
        [771515668,357571490,44788124,927702196,952509530]
    )
)
