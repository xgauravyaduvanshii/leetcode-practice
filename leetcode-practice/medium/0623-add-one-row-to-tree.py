# LeetCode 623. Add One Row to Tree — Medium
# https://leetcode.com/problems/add-one-row-to-tree/
# Submission 2198885707 — Accepted, Python3
#
# My thinking: at depth one the whole tree becomes
# the new root's left child. Any deeper, I walk
# down to the parents one level above the target
# depth and slip a new node in front of each of
# their children.

from __future__ import annotations

from typing import Optional


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        def add(node, level):
            if not node:
                return
            if level == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
            else:
                add(node.left, level + 1)
                add(node.right, level + 1)

        add(root, 1)
        return root
