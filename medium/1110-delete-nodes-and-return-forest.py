# LeetCode 1110. Delete Nodes And Return Forest — Medium
# https://leetcode.com/problems/delete-nodes-and-return-forest/
# Submission 2199000866 — Accepted, Python3
#
# My thinking: I walk the tree and cut out every
# deleted node. The children of a deleted node
# become new roots, and every other node stays
# with its parent.

from __future__ import annotations

from typing import List, Optional


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        delete = set(to_delete)
        forest = []

        def walk(node, is_root):
            if not node:
                return None
            if is_root and node.val not in delete:
                forest.append(node)
            node.left = walk(node.left, node.val in delete)
            node.right = walk(node.right, node.val in delete)
            return None if node.val in delete else node

        walk(root, True)
        return forest
