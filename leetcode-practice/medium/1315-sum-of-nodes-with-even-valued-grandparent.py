# LeetCode 1315. Sum of Nodes with Even-Valued Grandparent — Medium
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
# Submission 2199030972 — Accepted, Python3
#
# My thinking: I walk the tree carrying each
# node's parent and grandparent along. A node
# counts when its grandparent exists and is
# even.

from __future__ import annotations

from typing import Optional


class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        total = 0

        def walk(node, parent, grandparent):
            nonlocal total
            if not node:
                return
            if grandparent and grandparent.val % 2 == 0:
                total += node.val
            walk(node.left, node, parent)
            walk(node.right, node, parent)

        walk(root, None, None)
        return total
