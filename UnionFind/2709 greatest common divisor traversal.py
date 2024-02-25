import math
from collections import defaultdict


def canTraverseAllPairs(nums: list[int]) -> bool:
    if 1 in nums and len(nums) > 1:
        # Test Cases: [1, 1], [1]
        return False

    nums = list(set(nums))

    """

    # TLE!

    length = len(nums)
    parent = [i for i in range(length)]
    rank = [1 for _ in range(length)]

    def find(x: int) -> int:
        x_root = x
        while parent[x_root] != x_root:
            x_root = parent[x_root]
        return x_root

    def union(x: int, y: int):
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            elif rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            else:
                parent[x_root] = y_root
                rank[y_root] += 1

    def cal_divisors(num: int) -> set:
        # 唯一分解定理
        d = 2
        ans = set()
        while d ** 2 <= num:
            if num % d != 0:
                d += 1
            else:
                num = num // d
                ans.add(d)
        if num > 1:
            ans.add(num)
        return ans

    for i in range(length):
        for j in range(i+1, length):
            if math.gcd(nums[i], nums[j]) > 1:
                union(i, j)

    for i in range(length):
        parent[i] = find(parent[i])
    # print(parent)

    return len(set(parent)) == 1
    """

    # 参考第 952 题的解法：不是对 位置（index） 进行合并，而是对 约数（divisor） 进行合并。

    def cal_divisors(num: int) -> set:
        # 唯一分解定理
        d = 2
        ans = set()
        while d ** 2 <= num:
            if num % d != 0:
                d += 1
            else:
                num = num // d
                ans.add(d)
        if num > 1:
            ans.add(num)
        return ans

    primes = defaultdict(list)
    for i, e in enumerate(nums):
        for q in cal_divisors(e):
            primes[q].append(i)

    length = len(nums)
    parent = [i for i in range(length)]
    rank = [1 for _ in range(length)]

    def find(x: int) -> int:
        x_root = x
        while parent[x_root] != x_root:
            x_root = parent[x_root]
        return x_root

    def union(x: int, y: int):
        x_root = find(x)
        y_root = find(y)
        if x_root != y_root:
            if rank[x_root] > rank[y_root]:
                parent[y_root] = x_root
            elif rank[x_root] < rank[y_root]:
                parent[x_root] = y_root
            else:
                parent[x_root] = y_root
                rank[y_root] += 1

    for q in primes:
        for i in range(len(primes[q]) - 1):
            union(primes[q][i], primes[q][i + 1])

    for i in range(length):
        parent[i] = find(parent[i])
        # print(parent)

    return len(set(parent)) == 1


print(canTraverseAllPairs([2, 3, 6]))
print(canTraverseAllPairs([3, 9, 5]))
print(canTraverseAllPairs([4, 3, 12, 8]))
