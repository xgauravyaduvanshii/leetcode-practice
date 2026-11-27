# LeetCode 865. Smallest Subtree with all the Deepest Nodes — Medium
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/
# Submission 2198957466 — Accepted, Python3
#
# My thinking: I ask each subtree for its depth
# and its answer. When the two sides are equally
# deep, this node is the smallest one holding
# them all; otherwise the deeper side's answer
# wins.

from __future__ import annotations

from typing import Optional


class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def deepest(node):
            if not node:
                return (0, None)
            left_depth, left_node = deepest(node.left)
            right_depth, right_node = deepest(node.right)
            if left_depth > right_depth:
                return (left_depth + 1, left_node)
            if right_depth > left_depth:
                return (right_depth + 1, right_node)
            return (left_depth + 1, node)

        return deepest(root)[1]
