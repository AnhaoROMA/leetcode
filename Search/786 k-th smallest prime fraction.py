"""
https://leetcode.com/problems/k-th-smallest-prime-fraction/description/

https://youtu.be/ZzfXmZgJ0cw
"""


def main_function(arr: list[int], k: int) -> list[int]:
    """
    以 1 2 3 5 为例，

    -  1/2  1/3  1/5
    -   -   2/3  2/5
    -   -    -   3/5
    -   -    -    -

    a_{i, j} < a_{i+1, j}
    a_{i, j} < a_{i, j+1}
    """

    n = len(arr)
    l = 0
    r = 1.0
    while l < r:
        m = (l + r) / 2
        max_f = 0.0
        total = 0
        p = 0  # 记录当前最大元素的行
        q = 0  # 记录当前最大元素的列

        j = 1
        for i in range(n):
            while j < n and arr[i]/arr[j] > m:
                j += 1
            total += (n-j)
            if n == j:
                break
            f = arr[i] / arr[j]
            if f > max_f:
                p = i
                q = j
                max_f = f

        if total == k:
            return [arr[p], arr[q]]
        elif total > k:
            r = m
        else:
            l = m

    return [0, 0]


print(
    main_function(
        [1, 2, 3, 5],
        3
    )
)
