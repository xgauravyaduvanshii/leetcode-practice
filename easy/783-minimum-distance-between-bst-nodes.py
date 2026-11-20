# 783. Minimum Distance Between BST Nodes (Easy)
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
# Submission 2199964474 — Accepted, Python3
from __future__ import annotations

from typing import Optional


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # My thinking: an inorder walk of a search tree
        # visits values in order, so the smallest gap
        # between any two values must show up between two
        # neighbours in that walk. I keep the previous
        # value and the best gap seen so far.
        self.prev = None
        self.best = float("inf")

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            if self.prev is not None:
                self.best = min(self.best, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.best
