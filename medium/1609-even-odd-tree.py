# LeetCode 1609. Even Odd Tree — Medium
# https://leetcode.com/problems/even-odd-tree/
# Submission 2199891861 — Accepted, Python3
#
# My thinking: I walk level by level. Even
# levels need odd values strictly increasing;
# odd levels need even values strictly
# decreasing. The first level that breaks its
# rule fails the tree.

from __future__ import annotations
from collections import deque
from typing import Optional


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        level = 0
        while queue:
            previous = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if level % 2 == 0:
                    if node.val % 2 == 0 or (previous is not None and node.val <= previous):
                        return False
                else:
                    if node.val % 2 == 1 or (previous is not None and node.val >= previous):
                        return False
                previous = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return True
