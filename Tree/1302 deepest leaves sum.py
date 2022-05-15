"""
https://leetcode.com/problems/deepest-leaves-sum/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        last_floor = list()
        floor = list()
        floor.append(root)
        while len(floor) > 0:
            last_floor = floor
            floor = list()
            for node in last_floor:
                if node.left is not None:
                    floor.append(node.left)
                if node.right is not None:
                    floor.append(node.right)
        result = 0
        for node in last_floor:
            result += node.val
        return result