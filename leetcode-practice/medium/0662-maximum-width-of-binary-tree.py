# LeetCode 662. Maximum Width of Binary Tree — Medium
# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Submission 2198902082 — Accepted, Python3
#
# My thinking: I number the nodes like a heap —
# left child twice the parent, right child twice
# plus one. On each level the width is the gap
# between the first and last numbered node.

from __future__ import annotations

from collections import deque
from typing import Optional


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        widest = 0
        queue = deque([(root, 0)])
        while queue:
            widest = max(widest, queue[-1][1] - queue[0][1] + 1)
            for _ in range(len(queue)):
                node, position = queue.popleft()
                if node.left:
                    queue.append((node.left, 2 * position))
                if node.right:
                    queue.append((node.right, 2 * position + 1))
        return widest
