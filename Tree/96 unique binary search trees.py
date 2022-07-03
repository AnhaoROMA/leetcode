"""
https://leetcode.com/problems/unique-binary-search-trees/

Given an integer n,
return the number of structurally unique BST's (binary search trees)
which has exactly n nodes of unique values from 1 to n.

Input: n = 3
Output: 5

Input: n = 1
Output: 1
"""
mem = dict()
mem[0] = 1
mem[1] = 1


# Quick Sort的几何意义
# 先选中一值（root->value）作为根结点（root），
# 再计算出 root->left 有几个结点（设为left） 、 root->right 有几个结点（设为right）
# 由此计算出左侧共有 count(left) 种可能、右侧共有 count(right) 种可能
# 因此，以 root->value 为根结点时，共有 count(left) * count(right) 种可能
def count(n: int) -> int:
    if n in mem:
        return mem[n]
    result = 0
    for i in range(n):
        left = i
        right = n - 1 - i
        result += count(left) * count(right)
    mem[n] = result
    return result


print(count(19))
