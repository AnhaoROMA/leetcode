"""
https://leetcode.com/problems/get-the-maximum-score/

You are given two sorted arrays of distinct integers nums1 and nums2.

A valid path is defined as follows:
    Choose array nums1 or nums2 to traverse (from index-0).
    Traverse the current array from left to right.
    If you are reading any value that is present in nums1 and nums2,
        you are allowed to change your path to the other array.
        (Only one repeated value is considered in the valid path).
    The score is defined as the sum of uniques values in a valid path.

Return the maximum score you can obtain of all possible valid paths.
Since the answer may be too large, return it modulo 10^9+7.

Constraints:
    1 <= nums1.length, nums2.length <= 10^5
    1 <= nums1[i], nums2[i] <= 10^7
    nums1 and nums2 are strictly increasing.
"""


def maxSum(nums1: list[int], nums2: list[int]) -> int:
    """
    注意 nums1[] 和 nums2[] 均是严格单调递增的。

    当走到 x 点时，有两个选择：
    （1）继续往后走一步；
    （2）跳到另外一条线上（如果可以的话）；

    我的想法是，动态规划。
    以
        nums1 = [2, 4, 5, 8, 10]
        nums2 = [4, 6, 8, 9]
    为例，
    定义 dp[num] 表示以 num 为开头的 path 所能取得的最大 score 。
    那么按照顺序来：
        dp[10] = 10
        dp[9] = 9
        => dp[8] = 8 + max(dp[9], dp[10]) = 18
            => dp[6] = 6 + dp[8] = 24
            => dp[5] = 5 + dp[8] = 23
                => dp[4] = 4 + max(dp[5], dp[6]) = 28
                    => dp[2] = 2 + dp[4] = 30
    所以结果应该是 max(dp[2], dp[4]) = 30 。

    以
        nums1 = [1, 3, 5, 7, 9]
        nums2 = [3, 5, 100]
    为例，
    那么按照顺序来，
        dp[100] = 100
        dp[9] = 9
        dp[7] = 7 + dp[9] = 16
        => dp[5] = 5 + max(dp[7], dp[100]) = 105
            => dp[3] = 3 + dp[5] = 108
                => dp[1] = 1 + dp[3] = 109
    所以结果应该是 max(dp[1], dp[3]) = 109 。
    """
    dp = dict()
    length_1 = len(nums1)
    length_2 = len(nums2)
    i = length_1 - 1
    j = length_2 - 1
    while i > -1 or j > -1:
        # 只要还没遍访结束
        if i == -1:
            # i == -1 and j > -1
            if j == length_2 - 1:
                tmp_2 = 0
            else:
                tmp_2 = dp[nums2[j + 1]]
            dp[nums2[j]] = nums2[j] + tmp_2
            j -= 1
        elif j == -1:
            # i > -1 and j == -1
            if i == length_1 - 1:
                tmp_1 = 0
            else:
                tmp_1 = dp[nums1[i + 1]]
            dp[nums1[i]] = nums1[i] + tmp_1
            i -= 1
        else:
            # i > -1 and j > -1
            if nums1[i] > nums2[j]:
                if i == length_1-1:
                    tmp_1 = 0
                else:
                    tmp_1 = dp[nums1[i+1]]
                dp[nums1[i]] = nums1[i] + tmp_1
                i -= 1
            elif nums1[i] < nums2[j]:
                if j == length_2-1:
                    tmp_2 = 0
                else:
                    tmp_2 = dp[nums2[j+1]]
                dp[nums2[j]] = nums2[j] + tmp_2
                j -= 1
            else:
                # nums1[i] == nums2[j]
                if i == length_1-1:
                    tmp_1 = 0
                else:
                    tmp_1 = dp[nums1[i+1]]
                if j == length_2-1:
                    tmp_2 = 0
                else:
                    tmp_2 = dp[nums2[j+1]]
                dp[nums1[i]] = nums1[i] + max(tmp_1, tmp_2)
                i -= 1
                j -= 1
    # print(dp)
    return max(dp[nums1[0]], dp[nums2[0]]) % (10**9 + 7)


print(maxSum([2, 4, 5, 8, 10], [4, 6, 8, 9]))
print(maxSum([1, 3, 5, 7, 9], [3, 5, 100]))
print(maxSum([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
print(maxSum([2, 4, 5, 8, 9], [4, 6, 8, 9]))
