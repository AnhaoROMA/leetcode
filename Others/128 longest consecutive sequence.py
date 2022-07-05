"""
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
Therefore its length is 4.

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""


# solution：哈希表
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lib = set(nums)
        ans = 0
        for c in nums:
            if c in lib:
                count = 1
                lib.remove(c)
                target = c - 1
                while target in lib:
                    lib.remove(target)
                    count += 1
                    target -= 1
                target = c + 1
                while target in lib:
                    lib.remove(target)
                    count += 1
                    target += 1
                ans = max(ans, count)
        return ans
