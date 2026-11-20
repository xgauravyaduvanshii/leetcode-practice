# 501. Find Mode in Binary Search Tree (Easy)
# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# Submission 2199958395 — Accepted, Python3
from __future__ import annotations

from typing import List, Optional


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        # My thinking: an inorder walk of a binary search
        # tree visits values in sorted order, so equal
        # values sit side by side. I count each run as it
        # passes, and keep every value whose run is as
        # long as the longest seen so far.
        self.best = 0
        self.run = 0
        self.prev = None
        self.modes = []

        def visit(value):
            if value == self.prev:
                self.run += 1
            else:
                self.run = 1
                self.prev = value
            if self.run > self.best:
                self.best = self.run
                self.modes = [value]
            elif self.run == self.best:
                self.modes.append(value)

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            visit(node.val)
            inorder(node.right)

        inorder(root)
        return self.modes
