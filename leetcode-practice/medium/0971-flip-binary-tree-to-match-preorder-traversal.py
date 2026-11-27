# LeetCode 971. Flip Binary Tree To Match Preorder Traversal — Medium
# https://leetcode.com/problems/flip-binary-tree-to-match-preorder-traversal/
# Submission 2198979495 — Accepted, Python3
#
# My thinking: I walk the tree in preorder,
# checking each node against the voyage. When a
# node's left child is not the next value in the
# voyage, I flip the node and walk the right side
# first. A mismatch anywhere means it cannot be
# done.

from __future__ import annotations

from typing import List, Optional


class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        flips = []
        index = 0

        def walk(node):
            nonlocal index
            if not node:
                return True
            if node.val != voyage[index]:
                return False
            index += 1
            if node.left and node.left.val != voyage[index]:
                flips.append(node.val)
                return walk(node.right) and walk(node.left)
            return walk(node.left) and walk(node.right)

        return flips if walk(root) else [-1]
