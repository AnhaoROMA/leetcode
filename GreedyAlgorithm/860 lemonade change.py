"""
https://leetcode.com/problems/lemonade-change/
"""


def lemonade_change(bills: list[int]) -> bool:
    """
    贪心算法，先找最大面值的钱。
    """
    money = {
        5: 0,
        10: 0,
        20: 0
    }
    for bill in bills:
        money[bill] += 1
        should_change = bill - 5
        if should_change == 0:
            continue
        while should_change > 0:
            if should_change > 10 and money[10] > 0:
                should_change -= 10
                money[10] -= 1
            elif money[5] > 0:
                should_change -= 5
                money[5] -= 1
            else:
                return False
    return True


print(lemonade_change([5, 5, 10, 10, 20]))
print(lemonade_change([5, 5, 5, 10, 20]))
