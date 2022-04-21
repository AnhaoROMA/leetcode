MIN_VALUE = -1000001
MAX_VALUE = 1000001


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            temp = nums2
            nums2 = nums1
            nums1 = temp
        m = len(nums1)
        n = len(nums2)
        total_left = int((m + n + 1) / 2)

        left = 0
        right = m

        while left < right:
            i = left + int((right - left + 1) / 2)
            j = total_left - i
            if nums1[i - 1] < nums2[j]:
                left = i
            else:
                right = i - 1
        i = left
        j = total_left - i
        print(i)
        print(j)

        if i == 0:
            nums1_left = MIN_VALUE
        else:
            nums1_left = nums1[i - 1]

        if j == 0:
            nums2_left = MIN_VALUE
        else:
            nums2_left = nums2[j - 1]

        if i == m:
            nums1_right = MAX_VALUE
        else:
            nums1_right = nums1[i]

        if j == n:
            nums2_right = MAX_VALUE
        else:
            nums2_right = nums2[j]

        if (m + n) % 2 == 0:
            return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2.0
        else:
            return max(nums1_left, nums2_left)