# LeetCode 951. Flip Equivalent Binary Trees — Medium
# https://leetcode.com/problems/flip-equivalent-binary-trees/
# Submission 2198975840 — Accepted, Python3
#
# My thinking: two trees match when their roots
# are equal and their children match — either
# straight across, or swapped. I check both
# ways at every node.

from __future__ import annotations

from typing import Optional


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        same = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
        flipped = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
        return same or flipped
