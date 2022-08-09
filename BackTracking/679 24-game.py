"""
https://leetcode.com/problems/24-game/
"""


def judge(cards: list[int]) -> bool:
    if len(cards) == 1:
        return abs(cards[0]-24) < 0.00001
        
    for _ in range(len(cards)):
        a = cards.pop(0)  # 摸一张 (queue 操作)
        for _ in range(len(cards)):
            b = cards.pop(0)  # 再摸一张 (queue 操作)
            for value in [a + b, a - b, a * b, b and a / b]:  # 算一下
                cards.append(value)  # 记下来 (stack 操作)
                if judge(cards):
                    return True
                cards.pop()  # (stack 操作)
            cards.append(b)  # (queue 操作)
        cards.append(a)  # (queue 操作)
    return False


print(judge([3, 3, 8, 8]))
