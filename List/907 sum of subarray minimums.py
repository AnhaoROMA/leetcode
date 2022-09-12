"""
https://leetcode.com/problems/sum-of-subarray-minimums/
"""


def sum_subarray_min(arr: list[int]) -> int:
    """
    我们正向思维会想办法查找出所有的子数组然后求他的最小值。
    那么能不能换一种思路，我们找到一个值求解这个值能作为最小值作用的范围。
    """

    # mod = 10 ** 9 + 7
    # length = len(arr)
    # result = 0
    # for k in range(length):
    #     i = k - 1
    #     while i > -1:
    #         if arr[i] < arr[k]:
    #             break
    #         i -= 1
    #     j = k + 1
    #     while j < length:
    #         if arr[j] <= arr[k]:
    #             break
    #         j += 1
    #     # print(str(arr[k]) + ": " + str(i) + "^" + str(k) + "^" + str(j))
    #     result += (j - k) * (k - i) * arr[k]
    # return result % mod

    mod = 10 ** 9 + 7
    length = len(arr)
    # 使用单调栈
    monotonic_stack = list()
    # 计算当前元素 arr[i] 的左边第一个比 arr[i] 小的元素的下标
    prev = [0] * length
    for i in range(length):
        while monotonic_stack and arr[monotonic_stack[-1]] >= arr[i]:
            monotonic_stack.pop()
        if monotonic_stack:
            prev[i] = monotonic_stack[-1]
        else:
            prev[i] = -1
        monotonic_stack.append(i)
    # print(prev)
    # 计算当前元素 arr[i] 的右边第一个比 arr[i] 小的元素的下标
    monotonic_stack.clear()
    back = [0] * length
    for i in range(length-1, -1, -1):
        while monotonic_stack and arr[monotonic_stack[-1]] > arr[i]:
            monotonic_stack.pop()
        if monotonic_stack:
            back[i] = monotonic_stack[-1]
        else:
            back[i] = length
        monotonic_stack.append(i)
    # print(back)
    # 计算结果
    result = 0
    for i in range(length):
        result += (back[i]-i)*(i-prev[i])*arr[i]
    return result % mod


print(sum_subarray_min([3, 1, 2, 4]))
print(sum_subarray_min([11, 81, 94, 43, 3]))
