# LeetCode 1382. Balance a Binary Search Tree — Medium
# https://leetcode.com/problems/balance-a-binary-search-tree/
# Submission 2199044384 — Accepted, Python3
#
# My thinking: reading the tree in order gives
# its values sorted. I rebuild from the middle
# out, so the left and right halves stay even
# and the tree comes out balanced.

from __future__ import annotations

from typing import Optional


class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def collect(node):
            if node:
                collect(node.left)
                values.append(node.val)
                collect(node.right)

        collect(root)

        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(values[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(values) - 1)
