"""
https://leetcode.com/problems/longest-increasing-subsequence/

Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence
that can be derived from an array by deleting some or no elements
without changing the order of the remaining elements.

For example, [3, 6, 2, 7] is a subsequence of the array [0, 3, 1, 6, 2, 2, 7].

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [0,1,0,3,2,3]
Output: 4

Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""


# solution 1:
# O(N^2)
# DP Algorithm

# solution 2:
# O(NlgN)
# Greedy Algorithm
# 首先向列表中添加数组中首元素，然后从数组第二位开始顺序循环每一个数字。
# 如果 当前数字大于列表中最后一个元素的话，可以将该元素直接添加到列表中。
# 反之，
# 如果当前元素小于列表中最后一位时，我们采用二分方式找到列表中第一个大于等于当前数字的元素，并使用当前元素替换掉该元素。
# 原理在最下面。


def bin_search(target_list, target_value) -> int:
    start = 0
    end = len(target_list) - 1
    while start <= end:
        mid = (start + end) // 2
        if target_list[mid] == target_value:
            return mid
        elif target_list[mid] > target_value:
            end = mid - 1
        else:
            start = mid + 1
    return start


def lis(nums: list[int]) -> int:
    result = list()
    result.append(nums[0])
    length = len(nums)
    i = 1
    while i < length:
        if nums[i] > result[-1]:
            result.append(nums[i])
        else:
            substitute_index = bin_search(result, nums[i])
            result[substitute_index] = nums[i]
        i += 1
    return len(result)


a = [1, 2, 3, 4, 5, 6]
print(lis(a))
"""
举个例子，比如：[4,9,2,5,3,7,101,18]

1、首先将首元素4加入列表。 {4}
2、第二位9大于列表尾元素4，直接添加进列表。 {4，9}
3、第三位2小于列表尾元素9，从列表中找打第一个大于等于2的数字替换。 {2，9}（你对这一步也许会有疑问，暂且不论，后文阐述）
4、第四位5小于列表尾元素9，从列表中找打第一个大于等于5的数字替换。{2，5}
5、第五位3小于列表尾元素5，从列表中找打第一个大于等于3的数字替换。 {2，3}
6、第六位7大于列表尾元素3，直接添加进列表。{2，3，7}
7、第七位101大于列表尾元素7，直接添加进列表。{2，3，7，101}
8、第八位18小于列表尾元素101，从列表中找打第一个大于等于18的数字替换。 {2，3，7，18}

至此，列表元素个数定格为4，即本题返回结果。
接下来我们复盘一下该解法。
首先，如果当前数字大于列表尾元素时，将该元素直接加入列表的做法应该没有疑义。
争议较大的操作出现在上述第3步。
当时列表为{4，9}，当前数字为2，此时，找到列表中第一个大于等于2的数字为4，进而我们使用数字2替代了4，将列表更新为{2，9}。
这里你可能会有一个疑问，这样做是否正确？
比如当原始数组为[4,9,2]时，我们找到的最长子序列不是{4，9}，而是{2，9}。
虽然数组本身不正确，但数组的长度没有任何问题，因为本题求解的是子序列长度，所以我们可以忽视序列中元素的具体内容。
接下来我们详细看下为什么该算法求出的长度是正确的？

还以上文为例，当数字2出现时，显然不能和当前列表{4，9}组成一个新递增序列。
按照普通的想法，此时我们有2种选择，要么继续向后找比9大的数，要么，以2开头找一条新的路径。
我们使用2替换4的目的就是同时兼顾上述两种选择。
继续向后循环，当出现比9大的数字时，比如101，此时列表不论是{4，9，101}还是{2，9，101}，
这都不会影响列表的长度，只要我们知道9前面有一个数字小于它就是了，具体该数字是多少都不会改变9是当前列表中第二大数字的事实。
另一方面，如果当前出现了小于9但是大于2的数字时，比如5，此时，我们会使用5替换掉9，相当于以2开头重新找新的一条路路线去了。
此时数组会变为{2，5}。
"""
