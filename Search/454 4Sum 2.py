"""
https://leetcode.com/problems/4sum-ii/description/

Given four integer arrays nums1, nums2, nums3, and nums4, all of length n,
return the number of tuples (i, j, k, l)
such that:
    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Constraints:
    n == nums1.length
    n == nums2.length
    n == nums3.length
    n == nums4.length
    1 <= n <= 200
    -2^{28} <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^{28}
"""

from collections import Counter


def fourSumCount(nums1, nums2, nums3, nums4) -> int:
    """
    参考 two-sum 问题：
        当时只用了 O(n) 的时间复杂度
    这里我们可以采用“组合”的思想：
        (1)
            nums1 与 nums2 的所有组合的结果
                result_l = { nums1[i]+nums2[j] | -1 < i,j < n }
            nums3 与 nums4 的所有组合的结果
                result_r = { nums3[p]+nums4[q] | -1 < p,q < n }
        (2)
            对 result_l 与 result_r 采用 two-sum 的解法
    """
    n = len(nums1)
    result_l = []
    for i in range(n):
        for j in range(n):
            result_l.append(nums1[i] + nums2[j])
    result_r = []
    for i in range(n):
        for j in range(n):
            result_r.append(nums3[i] + nums4[j])
    result_l = Counter(result_l)
    result_r = Counter(result_r)
    answer = 0
    for cl in result_l:
        cr = -cl
        if cr in result_r:
            answer += result_l[cl] * result_r[cr]
    return answer


print(fourSumCount(nums1=[1,2], nums2=[-2,-1], nums3=[-1,2], nums4=[0,2]))
