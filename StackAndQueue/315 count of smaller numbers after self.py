"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

You are given an integer array nums
    and you have to return a new counts array.
The counts array has the property
    where counts[i] is the number of smaller elements to the right of nums[i].

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""


# 一开始的想法：哈希表，但是 TLE ！（47/65）
def main_hashmap(nums: list[int]) -> list[int]:
    ans = list()
    record = dict()
    i = len(nums) - 1
    while i >= 0:
        tmp = 0
        for r in record:
            if r < nums[i]:
                tmp += record[r]
        ans = [tmp] + ans
        if nums[i] in record:
            record[nums[i]] += 1
        else:
            record[nums[i]] = 1
        i -= 1
    return ans


# 解法：二分查找法
# 一开始设置一个单调递增的数组 record ，
# 从数组 nums 右侧开始，
# 将 nums[i] 插入到 record 中的恰当位置 j （保证单调递增）。
# 则 在 nums[i] 右侧、且比 nums[i] 小的元素共有 j 个。
def main(nums: list[int]) -> list[int]:
    ans = [-1 for _ in range(len(nums))]

    record = list()
    i = len(nums) - 1
    while i >= 0:
        num_i = nums[i]
        left = 0
        right = len(record)
        while left < right:
            mid = (left + right) // 2
            if record[mid] < num_i:
                left = mid + 1
            else:
                right = mid
        j = right
        record.insert(j, num_i)
        # record = record[:j] + [num_i] + record[j:]
        ans[i] = j
        i -= 1

    return ans


print(main([5, 2, 6, 1]))
print(main([-1, -1]))
