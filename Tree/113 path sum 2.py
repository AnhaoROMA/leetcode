"""
https://leetcode.com/problems/path-sum-ii/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = list()
        if root is None:
            return result
        bfs = list()
        bfs.append([[], root, targetSum])
        while len(bfs) > 0:
            temp_result, cur_node, left_value = bfs.pop(0)
            if cur_node.left is None and cur_node.right is None:
                if left_value - cur_node.val == 0:
                    temp_result.append(cur_node.val)
                    result.append(temp_result)
            else:
                if cur_node.left is not None:
                    tmp = list()
                    for e in temp_result:
                        tmp.append(e)
                    tmp.append(cur_node.val)
                    bfs.append([tmp, cur_node.left, left_value - cur_node.val])
                if cur_node.right is not None:
                    tmp = list()
                    for e in temp_result:
                        tmp.append(e)
                    tmp.append(cur_node.val)
                    bfs.append([tmp, cur_node.right, left_value - cur_node.val])
        return result
