# LeetCode 1123. Lowest Common Ancestor of Deepest Leaves — Medium
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
# Submission 2199001767 — Accepted, Python3
#
# My thinking: each subtree reports how deep it
# goes and the ancestor of its deepest leaves.
# When both sides are equally deep, their
# ancestor is this node; otherwise the deeper
# side's answer wins.

from __future__ import annotations

from typing import Optional


class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def walk(node):
            if not node:
                return 0, None
            left_depth, left_lca = walk(node.left)
            right_depth, right_lca = walk(node.right)
            if left_depth > right_depth:
                return left_depth + 1, left_lca
            if right_depth > left_depth:
                return right_depth + 1, right_lca
            return left_depth + 1, node

        return walk(root)[1]
