# 100. Same Tree (Easy)
# https://leetcode.com/problems/same-tree/
# Submission 2199956503 — Accepted, Python3
from __future__ import annotations

from typing import Optional


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # My thinking: two trees match when their roots
        # hold the same value and both pairs of children
        # match too. An empty tree only matches another
        # empty tree.
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )
