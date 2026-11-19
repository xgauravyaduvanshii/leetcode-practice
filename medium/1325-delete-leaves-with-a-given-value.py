# LeetCode 1325. Delete Leaves With a Given Value — Medium
# https://leetcode.com/problems/delete-leaves-with-a-given-value/
# Submission 2199032010 — Accepted, Python3
#
# My thinking: I clean the children first, so
# a parent that becomes a leaf gets checked
# too. Any leaf holding the target value is
# dropped.

from __future__ import annotations

from typing import Optional


class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        if not root.left and not root.right and root.val == target:
            return None
        return root
