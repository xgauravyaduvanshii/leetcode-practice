# LeetCode 701. Insert into a Binary Search Tree — Medium
# https://leetcode.com/problems/insert-into-a-binary-search-tree/
# Submission 2198916936 — Accepted, Python3
#
# My thinking: I walk down the tree, going left
# when the value is smaller and right when it is
# bigger, until I find an empty spot — that is
# where the new node belongs.

from __future__ import annotations

from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root
