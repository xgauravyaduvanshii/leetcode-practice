# LeetCode 1026. Maximum Difference Between Node and Ancestor — Medium
# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
# Submission 2198989126 — Accepted, Python3
#
# My thinking: I carry the smallest and largest
# ancestor values down the tree. At each node the
# best difference comes from one of those two
# extremes, then the node updates them for its
# children.

from __future__ import annotations

from typing import Optional


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        best = 0

        def walk(node, low, high):
            nonlocal best
            if not node:
                return
            best = max(best, abs(node.val - low), abs(node.val - high))
            low = min(low, node.val)
            high = max(high, node.val)
            walk(node.left, low, high)
            walk(node.right, low, high)

        walk(root, root.val, root.val)
        return best
