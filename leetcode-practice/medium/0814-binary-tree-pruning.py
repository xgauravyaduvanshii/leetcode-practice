# LeetCode 814. Binary Tree Pruning — Medium
# https://leetcode.com/problems/binary-tree-pruning/
# Submission 2198946499 — Accepted, Python3
#
# My thinking: I prune the children first, then
# decide about each node. A zero with no children
# left after pruning is useless, so it goes —
# everything else stays.

from __future__ import annotations

from typing import Optional


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root
