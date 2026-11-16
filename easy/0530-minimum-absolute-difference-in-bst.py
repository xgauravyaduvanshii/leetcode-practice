# LeetCode 530. Minimum Absolute Difference in BST — Easy
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# Submission 2197494250 — Accepted, Python3
#
# My thinking: an inorder walk of a BST visits the
# values in sorted order. So the smallest gap
# between any two values must be between two
# neighbours in that walk — I just compare each
# value with the one before it.

class Solution:
    def getMinimumDifference(self, root) -> int:
        self.previous = None
        self.min_diff = float('inf')

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.previous is not None:
                self.min_diff = min(self.min_diff, node.val - self.previous)
            self.previous = node.val
            inorder(node.right)

        inorder(root)
        return self.min_diff
