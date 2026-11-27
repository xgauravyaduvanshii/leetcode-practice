# LeetCode 687. Longest Univalue Path — Medium
# https://leetcode.com/problems/longest-univalue-path/
# Submission 2198910262 — Accepted, Python3
#
# My thinking: from each node I measure how far
# the same value runs down each side. The best
# path through that node joins both sides, and the
# best path overall is the biggest such join. The
# recursion limit is raised because the tree can
# be a thousand deep.

from __future__ import annotations

import sys
from typing import Optional

sys.setrecursionlimit(10000)


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def longest_down(node):
            if not node:
                return 0
            left = longest_down(node.left)
            right = longest_down(node.right)
            left_path = left + 1 if node.left and node.left.val == node.val else 0
            right_path = right + 1 if node.right and node.right.val == node.val else 0
            self.best = max(self.best, left_path + right_path)
            return max(left_path, right_path)

        longest_down(root)
        return self.best
