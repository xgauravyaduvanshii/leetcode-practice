# LeetCode 1261. Find Elements in a Contaminated Binary Tree — Medium
# https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/
# Submission 2199019109 — Accepted, Python3
#
# My thinking: the tree's true values follow a
# fixed rule — root zero, left child twice the
# parent plus one, right child twice plus two.
# I rebuild them all once and answer lookups
# from the set.

from __future__ import annotations

from typing import Optional


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.values = set()

        def recover(node, value):
            if not node:
                return
            self.values.add(value)
            recover(node.left, 2 * value + 1)
            recover(node.right, 2 * value + 2)

        recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values
