# LeetCode 998. Maximum Binary Tree II — Medium
# https://leetcode.com/problems/maximum-binary-tree-ii/
# Submission 2198983316 — Accepted, Python3
#
# My thinking: the new value belongs on the right
# spine. I walk down the right side until I find
# a smaller node — the new node takes its place,
# with that whole subtree hanging off its left.

from __future__ import annotations

from typing import Optional


class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or val > root.val:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        root.right = self.insertIntoMaxTree(root.right, val)
        return root
