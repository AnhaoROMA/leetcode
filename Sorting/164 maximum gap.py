"""
https://leetcode.com/problems/maximum-gap/

Given an integer array nums,
    return the maximum difference between two successive elements in its sorted form.
If the array contains less than two elements,
    return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Input:
    nums = [3,6,9,1]
Output:
    3
Explanation:
    The sorted form of the array is [1,3,6,9],
    either (3,6) or (6,9) has the maximum difference 3.

Input:
    nums = [10]
Output:
    0
Explanation:
    The array contains less than 2 elements, therefore return 0.

Constraints:
    1 <= nums.length <= 10^5
    0 <= nums[i] <= 10^9
"""

import math


def maximumGap(nums: list[int]) -> int:
    """
    桶排序 的 使用

    以 [ 0, 5, 10, 15, 20, 25, 30, 35, 40 ] 为例，
    9 items，8 gaps，
    其 max_gap = 5 。

    更一般的，[ 0, 3, 4, 6, 23, 28, 29, 33, 40 ]，
    9 items，8 gaps，
    其 max_gap > 5 。

    the fact:
        for 9 numbers in [0, 40] ( 8 gaps ),
        and min_item = 0 and max_item = 40 ,
        its max_gap >= 5 .
    proof:
        if max_gap < 5 , and in condition that all items are integer,
        then max_gap equals at most 4,
        then
            max_item-min_item <= 8*max_gap <= 32 .
        conflict with " min_item = 0 and max_item = 40 "!

    reference: https://zhuanlan.zhihu.com/p/92109072
    我们把 0 3 4 6 23 28 29 33 38 依次装到三个桶中，
        0            1            2           3
     -------      -------      -------     -------
    |  3 4  |    |       |    |  29   |   |  33   |
    |   6   |    |       |    |  23   |   |       |
    |   0   |    |       |    |  28   |   |  38   |
     -------      -------      -------     -------
      0 - 9       10 - 19      20 - 29     30 - 39
    我们把每个桶的最大值和最小值表示出来，
     min  max     min  max     min  max    min  max
     0     6       -    -      23   29     33   38
    我们可以只计算相邻桶的 min 和 max 的差值来解决问题（空桶直接跳过）。
    看起来没什么问题，但这样做一定需要一个前提：
        因为我们只计算了相邻桶的差值、而没有计算桶内数字的情况，
        所以我们需要保证每个桶里边的数字一定不会产生最大 gap ，即
            max_gap_{桶内} < max_gap_{桶间}
    我们把给定的数字中最小的是 min，最大的是 max，桶的范围大小为 interval，
    那么箱子划分的范围就是
        [min , min + 1 * interval)
        [min + 1 * interval , min + 2 * interval)
        [min + 2 * interval , min + 3 * interval)
        ... ... ...
    （ 上边举的例子中， interval 我们其实取了 10 ）
    划定了箱子范围后，我们其实很容易把数字放到箱子中：
        通过 (nums[i] - min) / interval 即可得到当前数字应该放到的箱子编号，
    那么最主要的问题其实就是怎么去确定（合适的） interval 。
        - interval 过小的话，需要更多的箱子去存储，很费空间，此外箱子增多了，比较的次数也会增多，不划算。
        - interval 过大的话，箱子内部的数字可能产生题目要求的最大 gap，所以肯定不行。
    所以我们要找到那个保证箱子内部的数字不会产生最大 gap，并且尽量大的 interval。
    继续看上边的例子，0 3 4 6 23 28 29 33 38，
    数组中的最小值 0 和最大值 38 ,并没有参与到 interval 的计算中，
    所以它俩可以不放到箱子中，还剩下 n-2 个数字。
    像上边的例子，如果我们保证至少有一个空箱子，那么我们就可以断言，箱子内部一定不会产生最大 gap。
        因为在我们的某次计算中，会跳过一个空箱子，那么得到的 gap 一定会大于 interval，
        而箱子中的数字最大的 gap 是 interval-1 。
    接下来的问题，怎么保证至少有一个空箱子呢？
    鸽巢原理的变形，有 n-2 个数字，如果箱子数多于 n-2 ，那么一定会出现空箱子。
    总范围是 max-min，那么 interval = (max-min)/箱子数，
    为了使得 interval 尽量大，箱子数取最小即可，也就是 n-1 。

    所以 interval = (max-min)/(n-1) 。这里如果除不尽的话，我们 interval 可以向上取整。
    因为我们给定的数字都是整数，这里向上取整的话对于最大 gap 是没有影响的：
        比如原来范围是 [0,5.5)，那么内部产生的最大 gap 是 5 - 0 = 5。
        现在向上取整，范围变成 [0,6)，但是内部产生的最大 gap 依旧是 5 - 0 = 5。
    """
    n = len(nums)
    if n <= 1:
        return 0
    min_nums = min(nums)
    max_nums = max(nums)
    if min_nums == max_nums:
        return 0
    interval = math.ceil((max_nums-min_nums)/(n-1))
    buckets = [{"min": None, "max": None} for _ in range(n-1)]
    # 将每个数字放进对应的桶中
    for i in range(n):
        index = (nums[i]-min_nums)//interval
        # 最大数和最小数不需要考虑
        if nums[i] == max_nums or nums[i] == min_nums:
            continue
        if buckets[index]["min"] is None or nums[i] < buckets[index]["min"]:
            buckets[index]["min"] = nums[i]
        if buckets[index]["max"] is None or nums[i] > buckets[index]["max"]:
            buckets[index]["max"] = nums[i]

    max_gap = 0
    previous_max = min_nums
    for i in range(n-1):
        if buckets[i]["max"] is None:
            continue
        max_gap = max(max_gap, buckets[i]["min"]-previous_max)
        previous_max = buckets[i]["max"]
    max_gap = max(max_gap, max_nums-previous_max)
    return max_gap


print(maximumGap([3,6,9,1]))
