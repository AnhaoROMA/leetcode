"""
https://leetcode.com/problems/sliding-window-median/

The median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value,
    so the median is the mean of the two middle values.
For examples, if arr = [2,3,4], the median is 3.
For examples, if arr = [1,2,3,4], the median is (2 + 3) / 2 = 2.5.

You are given an integer array nums and an integer k.
There is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the median array for each window in the original array.
Answers within 10^{-5} of the actual value will be accepted.

Input:
    nums = [1,3,-1,-3,5,3,6,7], k = 3
Output:
    [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation:
    Window position                Median
    ---------------                -----
    [1  3  -1] -3  5  3  6  7        1
     1 [3  -1  -3] 5  3  6  7       -1
     1  3 [-1  -3  5] 3  6  7       -1
     1  3  -1 [-3  5  3] 6  7        3
     1  3  -1  -3 [5  3  6] 7        5
     1  3  -1  -3  5 [3  6  7]       6

Input:
    nums = [1,2,3,4,2,3,1,4,2], k = 3
Output:
    [2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]

Constraints:
    1 <= k <= nums.length <= 10^5
    -2^{31} <= nums[i] <= 2^{31} - 1
"""

import heapq


def medianSlidingWindow(nums: list[int], k: int) -> list[float]:
    """
    单调栈
    """

    def binary_search(target: int) -> int:
        a = 0
        b = k
        while a < b:
            c = (a+b)//2
            if array[c] < target:
                a = c + 1
            else:
                b = c
        return a

    def binary_insert(target: int) -> int:
        a = 0
        b = k - 1
        while a < b:
            c = (a+b)//2
            if array[c] < target:
                a = c + 1
            else:
                b = c
        return a

    array = sorted(nums[:k])
    ans = []
    if k % 2 == 0:
        ans.append((array[k//2-1]+array[k//2])/2)
        for i in range(k, len(nums)):
            num = nums[i]
            temp = nums[i - k]
            where_to_pop = binary_search(temp)
            array.pop(where_to_pop)
            where_to_insert = binary_insert(num)
            array.insert(where_to_insert, num)
            ans.append((array[k//2-1]+array[k//2])/2)
    else:
        ans.append(array[k//2])
        for i in range(k, len(nums)):
            num = nums[i]
            temp = nums[i-k]
            where_to_pop = binary_search(temp)
            array.pop(where_to_pop)
            where_to_insert = binary_insert(num)
            array.insert(where_to_insert, num)
            ans.append(array[k//2])
    return ans


print(
    medianSlidingWindow(
        [1,3,-1,-3,5,3,6,7],
        3
    )
)
print(
    medianSlidingWindow(
        [1,3,-1,-3,5,3,6,7],
        5
    )
)
print(
    medianSlidingWindow(
        [1,3,-1,-3,5,3,6,7],
        2
    )
)
print(
    medianSlidingWindow(
        [1,3,-1,-3,5,3,6,7],
        4
    )
)
