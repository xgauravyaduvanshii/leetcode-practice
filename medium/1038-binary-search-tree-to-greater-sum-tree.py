# LeetCode 1038. Binary Search Tree to Greater Sum Tree — Medium
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
# Submission 2198990419 — Accepted, Python3
#
# My thinking: I walk the tree right to left, so
# I meet the biggest values first. A running
# total of everything seen so far becomes each
# node's new value.

from __future__ import annotations

from typing import Optional


class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        running = 0

        def walk(node):
            nonlocal running
            if not node:
                return
            walk(node.right)
            running += node.val
            node.val = running
            walk(node.left)

        walk(root)
        return root
