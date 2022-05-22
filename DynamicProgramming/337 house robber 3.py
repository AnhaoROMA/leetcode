"""
https://leetcode.com/problems/house-robber-iii/

The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that all houses in this place form a binary tree.
It will automatically contact the police
if two directly-linked houses were broken into on the same night.

Given the root of the binary tree,
return the maximum amount of money the thief can rob without alerting the police.
"""


# TLE
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        choice_1 = 0
        choice_1 += root.val
        if root.left is not None:
            choice_1 += self.rob(root.left.left)
            choice_1 += self.rob(root.left.right)
        if root.right is not None:
            choice_1 += self.rob(root.right.left)
            choice_1 += self.rob(root.right.right)

        choice_2 = 0
        if root.left is not None:
            choice_2 += self.rob(root.left)
        if root.right is not None:
            choice_2 += self.rob(root.right)

        return max(choice_1, choice_2)


# OK
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        # try:
        #     print(root.max)
        # except AttributeError:
        #     root.max = 1
        choice_1 = 0
        choice_1 += root.val
        if root.left is not None:
            # choice_1 += self.rob(root.left.left)
            # choice_1 += self.rob(root.left.right)
            if root.left.left is not None:
                try:
                    choice_1 += root.left.left.max
                except AttributeError:
                    root.left.left.max = self.rob(root.left.left)
                    choice_1 += root.left.left.max
            if root.left.right is not None:
                try:
                    choice_1 += root.left.right.max
                except AttributeError:
                    root.left.right.max = self.rob(root.left.right)
                    choice_1 += root.left.right.max
        if root.right is not None:
            # choice_1 += self.rob(root.right.left)
            # choice_1 += self.rob(root.right.right)
            if root.right.left is not None:
                try:
                    choice_1 += root.right.left.max
                except AttributeError:
                    root.right.left.max = self.rob(root.right.left)
                    choice_1 += root.right.left.max
            if root.right.right is not None:
                try:
                    choice_1 += root.right.right.max
                except AttributeError:
                    root.right.right.max = self.rob(root.right.right)
                    choice_1 += root.right.right.max

        choice_2 = 0
        if root.left is not None:
            try:
                choice_2 += root.left.max
            except AttributeError:
                root.left.max = self.rob(root.left)
                choice_2 += root.left.max
        if root.right is not None:
            try:
                choice_2 += root.right.max
            except AttributeError:
                root.right.max = self.rob(root.right)
                choice_2 += root.right.max

        root.max = max(choice_1, choice_2)
        return root.max
