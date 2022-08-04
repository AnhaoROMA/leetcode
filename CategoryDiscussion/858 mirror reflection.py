"""
https://leetcode.com/problems/mirror-reflection/
"""


from tokenize import maybe


def mirror_reflection(p: int, q: int) -> int:

    def one_step(cur_x: int, cur_y: int, last_x: int, last_y: int) -> list[int]:
        """
        由于在“入口”阶段，
        就已经排除了 (cur_x, cur_y) 在角落的可能，
        所以这里 (cur_x, cur_y) 仅可能在边上。

        同理，除了初始阶段，(last_x, last_y) 也仅可能在边上。
        """
        if cur_x == 0:
            # 此时在左侧边上
            # 分类讨论：
            # 如果 是从右上方来到这的
            #      那么之后会往右下方走，可能会落到下侧边，也可能落到右侧边   
            # 如果 是从右下方来到这的
            #      那么之后会往右上方走，可能会落到上侧边，也可能落到右侧边
            # （不可能是平行来的，下不再赘述）
            if last_y > cur_y:
                # 如果落在下侧边，则落在 (may_be, 0)
                may_be = (last_x*cur_y)/(last_y-cur_y)
                if may_be > p:
                    # 落于右侧边，落于 (p, may_be)
                    may_be = cur_y - (p*(last_y-cur_y))/last_x
                    return [p, may_be]
                else:
                    return [may_be, 0]
            else:
                # last_y < cur_y
                # 如果落在上侧边，则落在 (may_be, p)
                may_be = (last_x*(p-cur_y))/(cur_y-last_y)
                if may_be > p:
                    # 落于右侧边，落于 (p, may_be)
                    may_be = cur_y + (p*(cur_y-last_y))/last_x
                    return [p, may_be]
                else:
                    return [may_be, p]
        elif cur_x == p:
            # 此时在右侧边上
            if last_y > cur_y:
                may_be = p - (cur_y*(p-last_x))/(last_y-cur_y)
                if may_be < 0:
                    may_be = cur_y - (p*(last_y-cur_y))/(p-last_x)
                    return [0, may_be]
                else:
                    return [may_be, 0]
            else:
                may_be = p - ((p-last_x)*(p-cur_y))/(cur_y-last_y)
                if may_be < 0:
                    may_be = cur_y + (p*(cur_y-last_y))/(p-last_x)
                    return [0, may_be]
                else:
                    return [may_be, p]
        elif cur_y == 0:
            # 此时在下侧边上
            if last_x < cur_x:
                may_be = ((p-cur_x)*last_y)/(cur_x-last_x)
                if may_be > p:
                    may_be = cur_x + (p*(cur_x-last_x))/last_y
                    return [may_be, p]
                else:
                    return [p, may_be]
            else:
                may_be = (cur_x*last_y)/(last_x-cur_x)
                if may_be > p:
                    may_be = cur_x - (p*(last_x-cur_x))/last_y
                    return [may_be, p]
                else:
                    return [0, may_be]
        else:
            # cur_y == p
            # 此时在上侧边上
            if last_x < cur_x:
                may_be = cur_x + (p*(cur_x-last_x))/(p-last_y)
                if may_be > p:
                    may_be = p - ((p-last_y)*(p-cur_x))/(cur_x-last_x)
                    return [p, may_be]
                else:
                    return [may_be, 0]
            else:
                may_be = p - (cur_x*(p-last_y))/(last_x-cur_x)
                if may_be < 0:
                    may_be = cur_x - (p*(last_x-cur_x))/(p-last_y)
                    return [may_be, 0]
                else:
                    return [0, may_be]
    
    x = p  # cur_x
    y = q  # cur_y
    m = 0  # last_x
    n = 0  # last_y
    while True:
        if abs(x-p) < 0.0001 and abs(y) < 0.0001:
            # 此时位于右下角
            return 0
        elif abs(x-p) < 0.0001 and abs(y-p) < 0.0001:
            # 此时位于右上角
            return 1
        elif abs(x) < 0.0001 and abs(y-p) < 0.0001:
            # 此时位于左上角
            return 2
        else:
            [next_x, next_y] = one_step(x, y, m, n)
            m = x
            n = y
            x = next_x
            y = next_y


print(mirror_reflection(2, 1))
print(mirror_reflection(3, 1))
print(mirror_reflection(3, 2))
print(mirror_reflection(4, 3))
