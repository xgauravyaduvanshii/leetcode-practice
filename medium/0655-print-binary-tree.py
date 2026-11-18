# LeetCode 655. Print Binary Tree — Medium
# https://leetcode.com/problems/print-binary-tree/
# Submission 2198900199 — Accepted, Python3
#
# My thinking: the grid is as tall as the tree and
# as wide as a full tree of that height. Each node
# sits in the middle of its own slice of the grid,
# with its children centred in the halves beside
# it.

from __future__ import annotations

from typing import List, Optional


class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        def height(node):
            if not node:
                return 0
            return 1 + max(height(node.left), height(node.right))

        rows = height(root)
        cols = 2**rows - 1
        grid = [[""] * cols for _ in range(rows)]

        def fill(node, row, left, right):
            if not node:
                return
            mid = (left + right) // 2
            grid[row][mid] = str(node.val)
            fill(node.left, row + 1, left, mid - 1)
            fill(node.right, row + 1, mid + 1, right)

        fill(root, 0, 0, cols - 1)
        return grid
