# LeetCode 1367. Linked List in Binary Tree — Medium
# https://leetcode.com/problems/linked-list-in-binary-tree/
# Submission 2199041940 — Accepted, Python3
#
# My thinking: the list can start at any tree
# node, and from there it must follow a
# downward path matching link by link. I try
# every starting node and walk down both sides.

from __future__ import annotations

from typing import Optional


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def match(node, link):
            if not link:
                return True
            if not node or node.val != link.val:
                return False
            return match(node.left, link.next) or match(node.right, link.next)

        def search(node):
            if not node:
                return False
            return match(node, head) or search(node.left) or search(node.right)

        return search(root)
