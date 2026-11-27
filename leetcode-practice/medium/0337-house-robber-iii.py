# LeetCode 337. House Robber III — Medium
# https://leetcode.com/problems/house-robber-iii/
# Submission 2198749468 — Accepted, Python3
#
# My thinking: for each house I return two numbers
# — the best loot if I rob this house, and the best
# if I skip it. Robbing takes this house plus the
# skip-values of the children; skipping takes the
# best of each child. The root's best is the answer.

from typing import Optional


class Solution:
    def rob(self, root: "TreeNode") -> int:
        def best(node):
            if node is None:
                return (0, 0)
            left_rob, left_skip = best(node.left)
            right_rob, right_skip = best(node.right)
            rob_here = node.val + left_skip + right_skip
            skip_here = max(left_rob, left_skip) + max(right_rob, right_skip)
            return (rob_here, skip_here)

        return max(best(root))
