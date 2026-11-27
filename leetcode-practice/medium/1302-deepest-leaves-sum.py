# LeetCode 1302. Deepest Leaves Sum — Medium
# https://leetcode.com/problems/deepest-leaves-sum/
# Submission 2199027594 — Accepted, Python3
#
# My thinking: I walk the tree level by level
# and add up each level as I go. When there is
# no next level, the last sum I made is the
# deepest leaves' sum.

from __future__ import annotations

from typing import Optional


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        level = [root]
        while level:
            total = sum(node.val for node in level)
            level = [child for node in level for child in (node.left, node.right) if child]
        return total
