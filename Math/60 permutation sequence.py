"""
https://leetcode.com/problems/permutation-sequence/

The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the k-th permutation sequence.

Input: n = 3, k = 3
Output: "213"

Input: n = 4, k = 9
Output: "2314"

Input: n = 3, k = 1
Output: "123"
"""


# solution 1
# 参考第 31 题
# 单调栈的使用
def next_permutation(string: str) -> str:
    # 单调递增栈（队列）
    monotonic_queue = list()
    i = len(string) - 1
    while i >= 0:
        if not monotonic_queue or int(string[i]) > int(monotonic_queue[-1]):
            monotonic_queue.append(string[i])
        else:
            result = string[0:i]

            for j in range(len(monotonic_queue)):
                if int(monotonic_queue[j]) > int(string[i]):
                    break
            temp = monotonic_queue[j]
            monotonic_queue[j] = string[i]
            result += temp

            while monotonic_queue:
                temp = monotonic_queue.pop(0)
                result += temp
            return result
        i -= 1
    return string.reverse()


def solution(n: int, k: int) -> str:
    result = ""
    for i in range(1, n+1):
        result += str(i)
    for _ in range(k-1):
        result = next_permutation(result)
    return result


# solution 2
# 纯数学
def factorial(n: int):
    # 计算阶乘
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)


def count(n: int, k: int) -> str:
    result = list()
    leftovers = list()
    for i in range(1, n+1):
        leftovers.append(i)

    k -= 1  # 注意！
    i = 1
    while leftovers:
        divide = factorial(n - i)
        index = k // divide
        k -= index*divide
        result.append(leftovers[index])
        leftovers.pop(index)
        i += 1
    r = ""
    for num in result:
        r += str(num)
    return r


a = 3
b = 3
print(count(a, b))
