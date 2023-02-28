"""
https://leetcode.com/problems/fruit-into-baskets/

You are visiting a farm that has a single row of fruit trees arranged from left to right.
The trees are represented by an integer array fruits where fruits[i] is the type of fruit the i-th tree produces.

You want to collect as much fruit as possible.
However, the owner has some strict rules that you must follow:
    * You only have two baskets, and each basket can only hold a single type of fruit.
      There is no limit on the amount of fruit each basket can hold.
    * Starting from any tree of your choice,
      you must pick exactly one fruit from every tree (including the start tree) while moving to the right.
      The picked fruits must fit in one of your baskets.
    * Once you reach a tree with fruit that cannot fit in your baskets, you must stop.

Given the integer array fruits, return the maximum number of fruits you can pick.

Input: fruits = [1,2,1]
Output: 3

Input: fruits = [0,1,2,2]
Output: 3

Input: fruits = [1,2,3,2,2]
Output: 4

Input: fruits = [3,3,3,1,2,1,1,2,3,3,4]
Output: 5

Constraints:
    1 <= fruits.length <= 10^5
    0 <= fruits[i] < fruits.length
"""


def totalFruit(fruits: list[int]) -> int:
    """ O(2n) 的 贪心算法 """
    sorting = []  # sorting[i] = [fruit_type, fruit_count(fruit_type)]
    length = len(fruits)
    i = 0
    while i < length:
        j = i + 1
        while j < length and fruits[j] == fruits[i]:
            j += 1
        sorting.append([fruits[i], j - i])
        i = j
    # print(sorting)
    length = len(sorting)
    if length == 1:
        return sorting[0][1]
    result = 0
    i = 0
    while i < length - 1:
        j = i + 2
        while j < length and (sorting[j][0] == sorting[i][0] or sorting[j][0] == sorting[i+1][0]):
            j += 1
        temp_result = 0
        for k in range(i, j):
            temp_result += sorting[k][1]
        result = max(result, temp_result)
        i = j - 1
    return result


print(totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
print(totalFruit([0,1,2,2]))
