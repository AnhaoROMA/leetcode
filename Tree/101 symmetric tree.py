"""
https://leetcode.com/problems/symmetric-tree/
"""


class Solution:
    def compare(self, l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if l is None and r is None:
            return True
        elif l is not None and r is None:
            return False
        elif l is None and r is not None:
            return False
        else:
            return l.val == r.val and self.compare(l.right, r.left) and self.compare(r.right, l.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            return self.compare(root.left, root.right)
