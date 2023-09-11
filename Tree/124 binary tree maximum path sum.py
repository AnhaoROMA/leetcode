"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = -1001

    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        """
        如果设函数 dfs(node) 是求从 node 开始的单向树枝（只能向下走）的 max_sum ，
        那么 dfs(node) = max(node.val, node.val+dfs(node.left), node.val+dfs(node.right)) 。
                            “光秃秃的”     “选择左侧单向树枝”        “选择右侧单向树枝”

        当然本题的答案不是 dfs(root) ，因为 root 不一定出现在所求的 path 当中。

        在做 dfs(node) 的同时，也求出本体的答案 answer 。
        answer = max(
            answer,                                  # 到目前为止的最大解
            node.val,                                # 光秃秃的树根
            node.val+dfs(node.left),                 # 树根+左侧单向树枝
            node.val+dfs(node.right),                # 树根+右侧单向树枝
            node.val+dfs(node.left)+dfs(node.right)  # 树根+左侧单向树枝+右侧单向树枝
        )
        """

        def dfs(node: Optional[TreeNode]):

            if node.left is None:
                tmp_left = 0
            else:
                tmp_left = dfs(node.left)

            if node.right is None:
                tmp_right = 0
            else:
                tmp_right = dfs(node.right)

            self.ans = max(
                self.ans,
                node.val,
                node.val + tmp_left,
                node.val + tmp_right,
                node.val + tmp_left + tmp_right
            )

            return max(
                node.val,
                node.val + tmp_left,
                node.val + tmp_right
            )

        dfs(root)

        return self.ans
