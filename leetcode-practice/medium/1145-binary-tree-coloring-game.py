# LeetCode 1145. Binary Tree Coloring Game — Medium
# https://leetcode.com/problems/binary-tree-coloring-game/
# Submission 2199005291 — Accepted, Python3
#
# My thinking: the first player colours one
# node, which splits the tree into three parts
# — its left subtree, its right subtree, and
# everything above it. The second player wins
# by taking the biggest part.

from __future__ import annotations

from typing import Optional


class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def count(node):
            if not node:
                return 0
            return 1 + count(node.left) + count(node.right)

        def find(node):
            if not node:
                return None
            if node.val == x:
                return node
            return find(node.left) or find(node.right)

        target = find(root)
        left = count(target.left)
        right = count(target.right)
        parent_side = n - left - right - 1
        return max(left, right, parent_side) > n // 2
