"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        if root is None:
            return result
        else:
            result = self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

        return result
