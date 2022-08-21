"""
https://leetcode.com/problems/stamping-the-sequence/
"""


def moves_to_stamp(stamp: str, target: str) -> list[int]:
    """
    思想：
    1、在每个位置上，都最多只需要stamp一次，因为如果在同一个位置上stamp两次的话，前一次操作就白做了。
    2、如果从前向后转换的话，会有很多种可能，状态太多肯定也会超时。
    3、因此我们从结果往回推，”撕下“stamp后，将这些位置变为”*“，用于下一次匹配。
    """
    length_stamp = len(stamp)
    length_target = len(target)
    have_stamped = set()

    def is_matching(pos) -> bool:
        for k in range(length_stamp):
            if target[pos+k] == "*":
                continue
            else:
                if target[pos+k] != stamp[k]:
                    return False
                else:
                    continue
        return True

    steps = list()
    while target != "*"*length_target:
        stop = True
        for i in range(length_target-length_stamp+1):
            if i in have_stamped:
                continue
            if is_matching(i):
                stop = False
                steps = [i] + steps  # 因为我们是从后往前
                target = target[:i] + "*"*length_stamp + target[i+length_stamp:]
                have_stamped.add(i)
                break  # 记得要退出本次stamp
        if stop:
            steps = []
            break
    return steps


print(moves_to_stamp("abc", "ababc"))
print(moves_to_stamp("abca", "aabcaca"))
