"""
https://leetcode.com/problems/minimum-jumps-to-reach-home/

A certain bug's home is on the x-axis at position x.
Help them get there from position 0.

The bug jumps according to the following rules:
    It can jump exactly a positions forward (to the right).
    It can jump exactly b positions backward (to the left).
    It cannot jump backward twice in a row.
    It cannot jump to any forbidden positions.

The bug may jump forward beyond its home,
but it cannot jump to positions numbered with negative integers.

Given an array of integers forbidden,
where forbidden[i] means that the bug cannot jump to the position forbidden[i],
and integers a, b, and x, return the minimum number of jumps needed for the bug to reach its home.

If there is no possible sequence of jumps that lands the bug on position x, return -1.

Constraints:
    1 <= forbidden.length <= 1000
    1 <= a, b, forbidden[i] <= 2000
    0 <= x <= 2000
    All the elements in forbidden are distinct.
    Position x is not forbidden.
"""


def minimumJumps(forbidden: list[int], a: int, b: int, x: int) -> int:
    """
    很容易就想到 BFS 。

    但是有一个问题，就是如果不设置边界，就会无穷尽。
    读题可知，左边界（ left_border ）是 0 。
    令右边界（ right_border ）是 x+5000 。

    同样的，如果不设置 visited 机制，也会出现无穷尽的现象。
    比如 a=3, b=3, x=2 的情况。
    """
    forbidden = set(forbidden)

    left_border = 0
    right_border = x + 5000
    """
    下面这种写法是最保险的。
    # visited_by_forward = set()  <--  被（从左边）访问过。
    # visited_by_backward = set()  <--  被（从右边）访问过。
    
    能不能用一个 visited 呢？
    
    首先可以想到，
    如果一个位置被从左边访问过（ in visited_by_forward ），
    那么没有必要再去判断“从右边访问该位置”这种情况了。
    因为如果一个位置被从左边访问过，已经尝试过往左移和往右移两种情况了。
    而之后“从右边访问该位置”，只会尝试往右移，而这是之前已经尝试过了的。
    证毕！
    
    难点在于，
    如果一个位置被从右边访问过（ in visited_by_backward ），有没有必要再去判断“从左边访问该位置”这种情况？
    如果一个位置被从右边访问过，则当时只尝试过往右移。
    如果该位置在之后被从左边访问，则既需要尝试往左移（之前未尝试），也需要尝试往右移（已经尝试过）。
    
    当 a = b 时，
        会发现用一个 visited 就可以了，因为此时“一个位置被从右边访问过之后就不可能被从左边访问”。
    当 a > b 时，
        会发现用一个 visited 就可以了，因为此时“一个位置被从右边访问过之后就不可能被从左边访问”。
    当 a < b 时，
        （ 我们只关心会不会影响结果。）
        假设该位置为 X ，其已被从右边（ X+b ）访问过。
        注意，由于不能连续两次左移，说明 X+b 是被从左边（ X+b-a ）访问 ！
        记访问 X+b-a 的时刻为 t{0} 、每次都先尝试向左移动。
        
        情形一、t{-1}时刻在 X+b-2a （ X+b-a 被从左边访问 ）
            得到：t{1}时刻入 BFS 的顺序是 X-a （ visited_by_backward ） 、X+b （ visited_by_forward ）。
                 t{2}时刻入 BFS 的顺序是 X（visited_by_forward）、X（visited_by_backward）、X+b+a（visited_by_forward）。
                     <- 注意，优先保证了 visited_by_forward ，这点很关键！
            你发现了什么？
            在“每次都先尝试向左移动”的前提下，X 永远会优先被 visited_by_forward ！
            此时，用一个 visited 就可以了。
            （已验证：若每次优先尝试向右移，会有 wrong answer 。）
        
        情形二、t{-1}时刻在 X+2b-a （ X+b-a 被从右边访问 ）
            同样的方法，可知 X+2b-a 被从左边（ X+2b-2a ）访问。
            若 X+2b-2a 被从左边访问，则 X+b-a 会优先被 visited_by_forward ，这与假设“X+b-a 被从右边访问”矛盾！
            则推导出 X+2b-2a 被从右边访问。
            这将是个无极问题：X+nb-na 被从右边访问。
            但是！对于极点，它一定又得是从原点不断右移得来，矛盾！
        
        综上所述，在保证“每次都先尝试向左移动”的前提下，只需要一个 visited ，证毕！
    
    综上所述，在保证“每次都先尝试向左移动”的前提下，只需要一个 visited ，证毕！
    """
    visited = set()
    bfs = [
        {
            "pos": 0,  # 现在的位置
            "moves": 0,  # 已经行动的步数
            "cannot_backward": False  # 这一次能不能往左走
        }
    ]
    visited.add(0)
    while bfs:
        temp = bfs.pop(0)
        if temp["pos"] == x:
            return temp["moves"]
        # 尝试向左移
        if temp["cannot_backward"] is False:
            tmp = temp["pos"] - b
            if tmp >= left_border and tmp not in forbidden and tmp not in visited:
                bfs.append(
                    {
                        "pos": tmp,
                        "moves": temp["moves"]+1,
                        "cannot_backward": True
                    }
                )
                visited.add(tmp)
        # 尝试向右移
        tmp = temp["pos"] + a
        if tmp <= right_border and tmp not in forbidden and tmp not in visited:
            bfs.append(
                {
                    "pos": tmp,
                    "moves": temp["moves"] + 1,
                    "cannot_backward": False
                }
            )
            visited.add(tmp)
    return -1


print(
    minimumJumps(
        [1, 6, 2, 14, 5, 17, 4],
        16,
        9,
        7
    )
)
print(
    minimumJumps(
        [],
        3,
        3,
        2
    )
)
