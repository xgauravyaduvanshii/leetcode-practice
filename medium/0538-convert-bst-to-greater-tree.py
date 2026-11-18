# LeetCode 538. Convert BST to Greater Tree — Medium
# https://leetcode.com/problems/convert-bst-to-greater-tree/
# Submission 2198858295 — Accepted, Python3
#
# My thinking: in a binary search tree the greater
# values sit to the right, so a reverse in-order
# walk meets them biggest first. I keep a running
# total and add it into each node as I pass.

from __future__ import annotations

from typing import Optional


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total = 0

        def reverse_inorder(node):
            nonlocal total
            if not node:
                return
            reverse_inorder(node.right)
            total += node.val
            node.val = total
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root
