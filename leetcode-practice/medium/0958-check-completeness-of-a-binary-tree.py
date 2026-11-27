# LeetCode 958. Check Completeness of a Binary Tree — Medium
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
# Submission 2198976697 — Accepted, Python3
#
# My thinking: in a complete tree, every level
# is filled left to right. I walk level by level
# — once I meet a missing node, no real node may
# appear after it.

from __future__ import annotations

from collections import deque
from typing import Optional


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        gap_seen = False
        while queue:
            node = queue.popleft()
            if not node:
                gap_seen = True
            else:
                if gap_seen:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True
