# LeetCode 110. Balanced Binary Tree — Easy
# https://leetcode.com/problems/balanced-binary-tree/
# Submission 2197388246 — Accepted, Python3
#
# My thinking: a tree is balanced when both children are
# balanced and their heights differ by at most one. I let
# the height function return -1 as a signal that a subtree
# is already unbalanced, so the bad news travels straight up.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # A tree is balanced if both children are balanced and their heights
        # differ by at most 1. Return -1 up the chain to signal imbalance.
        def height(node):
            if not node:
                return 0
            left = height(node.left)
            if left == -1:
                return -1
            right = height(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return height(root) != -1
