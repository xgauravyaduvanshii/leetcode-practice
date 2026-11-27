# LeetCode 1008. Construct Binary Search Tree from Preorder Traversal — Medium
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
# Submission 2198985894 — Accepted, Python3
#
# My thinking: I read the preorder values one by
# one and build the tree down from the top. A
# value belongs in the left subtree only while
# it is smaller than its parent — anything bigger
# stops that branch.

from __future__ import annotations

from typing import List, Optional


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        index = 0

        def build(upper):
            nonlocal index
            if index == len(preorder) or preorder[index] > upper:
                return None
            node = TreeNode(preorder[index])
            index += 1
            node.left = build(node.val)
            node.right = build(upper)
            return node

        return build(float("inf"))
