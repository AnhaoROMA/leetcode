"""
https://leetcode.com/problems/path-sum/

Given the root of a binary tree and an integer targetSum,
return true if the tree has a root-to-leaf path
such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        bfs = list()
        bfs.append([root, targetSum])
        while len(bfs) > 0:
            cur_node, left_value = bfs.pop(0)
            if cur_node.left is None and cur_node.right is None:
                if left_value - cur_node.val == 0:
                    return True
            else:
                if cur_node.left is not None:
                    bfs.append([cur_node.left, left_value - cur_node.val])
                if cur_node.right is not None:
                    bfs.append([cur_node.right, left_value - cur_node.val])
        return False
