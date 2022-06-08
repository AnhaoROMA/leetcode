"""
https://leetcode.com/problems/combinations/

Given two integers n and k,
return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

Input: n = 1, k = 1
Output: [[1]]

Constraints:
    1 <= n <= 20
    1 <= k <= n
"""


def combinations_dfs(n: int, k: int) -> list[list[int]]:
    result = list()
    for i in range(1, n+1):
        if n < k:
            continue
        else:
            all_elements = [j for j in range(1, i+1)]
            dfs = [
                [[], all_elements]
            ]
            while dfs:
                temp_result, left_elements = dfs.pop()
                if len(temp_result) == k and temp_result not in result:
                    result.append(temp_result)
                else:
                    length = len(left_elements)
                    for j in range(length):
                        if len(temp_result) + (length - j) >= k:
                            dfs.append(
                                [
                                    temp_result + [left_elements[j]],
                                    left_elements[j+1:]
                                ]
                            )
                        else:
                            break
    return result


print(combinations_dfs(4, 2))
