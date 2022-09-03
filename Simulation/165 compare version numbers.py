"""
https://leetcode.com/problems/compare-version-numbers/
"""


def compare_version(v_1: str, v_2: str) -> int:

    def version(v: str) -> list[int]:
        parts = v.split(".")
        for i, part in enumerate(parts):
            parts[i] = int(part)
        while parts and parts[-1] == 0:
            parts.pop()
        return parts

    v_1 = version(v_1)
    v_2 = version(v_2)
    while v_1 and v_2:
        tmp_1 = v_1.pop(0)
        tmp_2 = v_2.pop(0)
        if tmp_1 > tmp_2:
            return 1
        elif tmp_1 < tmp_2:
            return -1
        else:
            continue
    if not v_1 and not v_2:
        return 0
    elif v_1:
        return 1
    else:
        return -1


print(compare_version("1.01", "1.001"))
print(compare_version("1.0", "1.0.0"))
print(compare_version("0.1", "1.1"))
