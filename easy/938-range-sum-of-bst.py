# 938. Range Sum of BST (Easy)
# https://leetcode.com/problems/range-sum-of-bst/
# Submission 2199965318 — Accepted, Python3
from __future__ import annotations

from typing import Optional


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # My thinking: walk the tree, adding every value
        # inside the range. The search-tree order tells
        # me which sides can be skipped: a node below the
        # range has nothing useful on its left, and a
        # node above it has nothing on its right.
        if root is None:
            return 0
        total = 0
        if low <= root.val <= high:
            total += root.val
        if root.val > low:
            total += self.rangeSumBST(root.left, low, high)
        if root.val < high:
            total += self.rangeSumBST(root.right, low, high)
        return total
