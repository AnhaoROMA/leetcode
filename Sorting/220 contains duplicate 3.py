"""
https://leetcode.com/problems/contains-duplicate-iii/

You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:
    i != j
    abs(i - j) <= indexDiff
    abs(nums[i] - nums[j]) <= valueDiff

Return true if such pair exists or false otherwise.

Input:
    nums = [1,2,3,1], indexDiff = 3, valueDiff = 0
Output:
    true
Explanation:
    We can choose (i, j) = (0, 3).
    We satisfy the three conditions:
        i != j --> 0 != 3
        abs(i - j) <= indexDiff --> abs(0 - 3) <= 3
        abs(nums[i] - nums[j]) <= valueDiff --> abs(1 - 1) <= 0

Input:
    nums = [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3
Output:
    false
Explanation:
    After trying all the possible pairs (i, j),
    we cannot satisfy the three conditions,
    so we return false.

Constraints:
    2 <= nums.length <= 10^5
    -10^9 <= nums[i] <= 10^9
    1 <= indexDiff <= nums.length
    0 <= valueDiff <= 10^9
"""


def containsNearbyAlmostDuplicate(nums: list[int], indexDiff: int, valueDiff: int) -> bool:
    """
    桶排序

    假如没有 indexDiff 的限制呢？
    定义桶的大小是 valueDiff+1 ， 通过 nums[i]//(valueDiff+1) 决定放入几号桶，
    这样在一个桶里面的任意两个的绝对值差值都 <= valueDiff 。
    例如
        valueDiff=3，nums=[0 ,5, 1, 9, 3, 4]，
        那么0号桶就有 [0, 1, 3]，1号桶就有 [4, 5]，2号桶就有 [9]。
    先不考虑 indexDiff 的限制，那么遍历 nums 每一个元素，并把他们放入相应的桶中，有两种情况会返回 True 。
        要放入的桶中已经有其他元素了，这时将 nums[i] 放进去满足差值 <=valueDiff 。
        可能存在前面一个桶的元素并且与 nums[i] 的差值 <=valueDiff 或者 存在后面一个桶的元素并且与 nums[i] 的差值 <=valueDiff 。
    根据返回 True 的第一个条件，可以知道前后桶的元素最多也只能有一个。

    接着考虑 indexDiff 的限制。
    当 i>=indexDiff 的时候，我们就要去删除存放着 nums[i-indexDiff] 的那个桶（编号为nums[i-indexDiff]//(valueDiff+1)）。
    这样就能保证遍历到第 i+1 个元素时，全部桶中元素的索引最小值是 i-indexDiff+1，就满足题目对索引的限制了。
    """
    bucket_size = valueDiff + 1
    all_buckets = dict()
    for i in range(len(nums)):
        # 放入哪个桶
        bucket_index = nums[i] // bucket_size

        if bucket_index in all_buckets:
            # 该桶中已经有元素了
            return True
        if bucket_index-1 in all_buckets and abs(all_buckets[bucket_index-1]-nums[i]) <= valueDiff:
            # 检查前一个桶
            return True
        if bucket_index+1 in all_buckets and abs(all_buckets[bucket_index+1]-nums[i]) <= valueDiff:
            # 检查后一个桶
            return True

        # 把 nums[i] 放入对应的桶中
        all_buckets[bucket_index] = nums[i]

        # 如果不构成返回条件，那么当 i >= indexDiff 的时候就要删除旧桶了，以维持桶中的元素索引跟下一个 i+1 索引只差不超过 indexDiff 。
        if i >= indexDiff:
            all_buckets.pop(nums[i-indexDiff] // bucket_size)

    return False


print(containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))
