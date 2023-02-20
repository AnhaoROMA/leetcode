"""
https://leetcode.com/problems/longest-univalue-path/

Given the root of a binary tree,
return the length of the longest path, where each node in the path has the same value.
This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        """
        这一题可以与第 375 题和第 965 题放在一起看。

        思想就是，
            我的行动与我的目标结果看上去没有关系，但是在我行动的同时，我也得到了想要的结果。
        """

        self.result = 0
        if root is None:
            return self.result

        def dfs(x: Optional[TreeNode]) -> List[int]:
            """
            [m, n] = dfs(node)
                m 表示以 node.left 为某个 path 中的一环时，这条 path 以 node 为界、左右两支各自最多可以有多长(不能再向上经过 node 本身)；
                n 表示以 node.right 为某个 path 中的一环时，这条 path 以 node 为界、左右两支各自最多可以有多长(不能再向上经过 node 本身)；

            以下图为例。

                           5 (m=0, n=2)
                          / \
                         v   v
             (m=0, n=0) 4     5 (m=0, n=1)
                       / \     \
                      v   v     v
                      1   1      5

                           1 (m=0, n=0)
                          / \
              (m=1, n=1) 4   5 (m=0, n=1)
                        / \   \
            (m=0, n=0) 4   4   5 (m=0, n=0)
                      (m=0, n=0)

            当 node.left 与 node.right 均不为 None 时，
            令
                [m1, n1] = dfs(node.left)
                [m2, n2] = dfs(node.right)
            则
                dfs(node) = [m, n]
            其中
                如果 node.left.val == node.val
                    m = 1 + max(m1, n1)
                否则
                    m = 0
                如果 node.right.val == node.val
                    n = 1 + max(m2, n2)
                否则
                    n = 0
            """
            if x.left is None and x.right is None:
                m = 0
                n = 0
                return [m, n]
            elif x.left is None and x.right is not None:
                m = 0
                if x.val != x.right.val:
                    n = 0
                    dfs(x.right)  # 仍然要DFS
                else:
                    n = 1 + max(dfs(x.right))
                self.result = max(self.result, n)
                return [m, n]
            elif x.left is not None and x.right is None:
                if x.val != x.left.val:
                    m = 0
                    dfs(x.left)  # 仍然要DFS
                else:
                    m = 1 + max(dfs(x.left))
                n = 0
                self.result = max(self.result, m)
                return [m, n]
            else:
                # x.left is not None and x.right is not None
                if x.val != x.left.val:
                    m = 0
                    dfs(x.left)  # 仍然要DFS
                else:
                    m = 1 + max(dfs(x.left))
                if x.val != x.right.val:
                    n = 0
                    dfs(x.right)  # 仍然要DFS
                else:
                    n = 1 + max(dfs(x.right))
                self.result = max(self.result, m + n)
                return [m, n]

        dfs(root)
        return self.result
