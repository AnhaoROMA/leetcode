"""
https://leetcode.com/problems/binary-trees-with-factors/

Given an array of unique integers, arr,
where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers,
and each number may be used for any number of times.
Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make.
The answer may be too large so return the answer modulo 10^9+7.

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]

Input: arr = [2,4,5,10]
Output: 7
Explanation: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].

Constraints:
    1 <= arr.length <= 1000
    2 <= arr[i] <= 10^9
    All the values of arr are unique.
"""


def count(arr: list[int]) -> int:
    arr.sort()
    # print(arr)
    length = len(arr)
    max_element = arr[-1]
    factorizations = {
        arr[i]: [] for i in range(length)
    }
    for i in range(length):
        if arr[i]*arr[i] > max_element:
            break
        for j in range(i, length):
            if arr[i]*arr[j] > max_element:
                break
            if arr[i]*arr[j] in arr:
                factorizations[arr[i]*arr[j]].append((arr[i], arr[j]))
                if i != j:
                    factorizations[arr[i]*arr[j]].append((arr[j], arr[i]))
    # print(factorizations)
    
    # mem[i]: 以 i 为根节点时，有多少种情况。
    mem = {}
    
    def helping_hand(n: int) -> None:
        """
        计算以 n 为根节点时，有多少种情况。
        """
        if n not in mem:
            result = 0
            result += 1  # 只有它一个节点
            for fac in factorizations[n]:
                result += helping_hand(fac[0])*helping_hand(fac[1])
            mem[n] = result
        return mem[n]
    
    # 填充 mem[]
    for element in arr:
        helping_hand(element)
    print(mem)
    return sum(mem.values())

print(count([3, 9, 27, 729]))
