"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = list()
        stack = list()
        while root is not None or len(stack) != 0:
            while root is not None:
                stack.append(root)
                result.append(root.val)
                root = root.left
            root = stack.pop()

            root = root.right
        return result
