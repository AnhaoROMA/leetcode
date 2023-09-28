"""
You are given an integer array nums of length n
    where nums is a permutation of the numbers in the range [0, n-1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:
    The first element in s[k] starts with the selection of the element nums[k] of index = k.
    The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
    We stop adding right before a duplicate element occurs in s[k].

Return the longest length of a set s[k].

Input:
    nums = [5,4,0,3,1,6,2]
Output:
    4
Explanation:
    nums[0] = 5, nums[1] = 4, nums[2] = 0, nums[3] = 3, nums[4] = 1, nums[5] = 6, nums[6] = 2.
    One of the longest sets s[k]:
        s[0] = {nums[0], nums[5], nums[6], nums[2]} = {5, 6, 2, 0}

Input:
    nums = [0,1,2]
Output:
    1

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] < nums.length
    All the values of nums are unique.
"""

from collections import Counter


def arrayNesting(nums: list[int]) -> int:

    """
    利用 并查集 求 子图的规模
    """

    n = len(nums)

    parent = [i for i in range(n)]
    rank = [1 for _ in range(n)]

    def find_root(node: int) -> int:
        node_root = node
        while node_root != parent[node_root]:
            node_root = parent[node_root]
        return node_root

    def union(x: int, y: int):
        x_root = find_root(x)
        y_root = find_root(y)
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root
            rank[y_root] += 1

    for i in range(n):
        union(i, nums[i])
    for i in range(n):
        parent[i] = find_root(i)
    result = Counter(parent)
    ans = 1
    for i in result:
        ans = max(ans, result[i])
    return ans


print(arrayNesting([5,4,0,3,1,6,2]))
print(arrayNesting([0,1,2]))
