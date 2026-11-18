# LeetCode 979. Distribute Coins in Binary Tree — Medium
# https://leetcode.com/problems/distribute-coins-in-binary-tree/
# Submission 2198980209 — Accepted, Python3
#
# My thinking: every subtree must end up with
# exactly as many coins as nodes. I ask each
# child how many coins it has spare or needs, and
# every coin that crosses an edge is one move.

from __future__ import annotations

from typing import Optional


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        moves = 0

        def balance(node):
            nonlocal moves
            if not node:
                return 0
            left = balance(node.left)
            right = balance(node.right)
            moves += abs(left) + abs(right)
            return node.val + left + right - 1

        balance(root)
        return moves
