"""
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u_i, v_j) with the smallest sums.

Input:
    nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output:
    [[1,2],[1,4],[1,6]]
Explanation:
    The first 3 pairs are returned from the sequence:
        [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

Input:
    nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output:
    [[1,1],[1,1]]
Explanation:
    The first 2 pairs are returned from the sequence:
        [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Input:
    nums1 = [1,2], nums2 = [3], k = 3
Output:
    [[1,3],[2,3]]
Explanation:
    All possible pairs are returned from the sequence:
        [1,3],[2,3]

Constraints:
    1 <= nums1.length, nums2.length <= 10^5
    -10^9 <= nums1[i], nums2[i] <= 10^9
    nums1 and nums2 both are sorted in ascending order.
    1 <= k <= 10^4
"""

import heapq


def kSmallestPairs(nums1: list[int], nums2: list[int], k: int) -> list[list[int]]:
    """
    一开始我想成了“双指针、求 what's next 问题”，
    后来看答案发现原来只是 BFS 。。。
    """
    h = [(nums1[0]+nums2[0], 0, 0)]
    seen = set((0,0))
    res = []
    while h and len(res) < k:
        total, i, j = heapq.heappop(h)
        res.append([nums1[i], nums2[j]])
        if i < len(nums1)-1 and (i+1, j) not in seen:
            heapq.heappush(h, (nums1[i+1]+nums2[j], i+1, j))
            seen.add((i+1, j))
        if j < len(nums2)-1 and (i, j+1) not in seen:
            heapq.heappush(h, (nums1[i]+nums2[j+1], i, j+1))
            seen.add((i, j+1))
    return res


print(kSmallestPairs(nums1=[1,2,4], nums2=[-1,1,2], k=100))
print(kSmallestPairs(nums1=[1,7,11], nums2=[2,4,6], k=10))
print(kSmallestPairs(nums1=[1,1,2], nums2=[1,2,3], k=20))
print(kSmallestPairs(nums1=[1,2], nums2=[3], k=10))
