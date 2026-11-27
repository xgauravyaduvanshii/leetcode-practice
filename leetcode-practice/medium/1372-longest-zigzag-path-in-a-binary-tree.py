# LeetCode 1372. Longest ZigZag Path in a Binary Tree — Medium
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
# Submission 2199042656 — Accepted, Python3
#
# My thinking: I walk the tree carrying the
# length of the zigzag that arrived from the
# left and from the right. Going left extends
# the right-arriving path, and going right
# extends the left-arriving one.

from __future__ import annotations

from typing import Optional


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def walk(node, left_len, right_len):
            if not node:
                return
            self.best = max(self.best, left_len, right_len)
            walk(node.left, right_len + 1, 0)
            walk(node.right, 0, left_len + 1)

        walk(root, 0, 0)
        return self.best
