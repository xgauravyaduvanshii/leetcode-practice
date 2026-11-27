# LeetCode 1080. Insufficient Nodes in Root to Leaf Paths — Medium
# https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/
# Submission 2198997038 — Accepted, Python3
#
# My thinking: I walk down from the root,
# carrying the limit that is left. A leaf stays
# only if its own value reaches the limit; a
# parent stays only if at least one of its
# children does.

from __future__ import annotations

from typing import Optional


class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        if not root:
            return None
        if not root.left and not root.right:
            return root if root.val >= limit else None
        root.left = self.sufficientSubset(root.left, limit - root.val)
        root.right = self.sufficientSubset(root.right, limit - root.val)
        return root if root.left or root.right else None
