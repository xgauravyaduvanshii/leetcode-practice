# LeetCode 1161. Maximum Level Sum of a Binary Tree — Medium
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Submission 2199008513 — Accepted, Python3
#
# My thinking: I walk the tree one level at a
# time, adding up each level as I go, and keep
# the level with the biggest sum — the smallest
# such level if two tie.

from __future__ import annotations

from collections import deque
from typing import Optional


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        best_level = 1
        best_sum = root.val
        level = 1
        while queue:
            level_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level_sum > best_sum:
                best_sum = level_sum
                best_level = level
            level += 1
        return best_level
