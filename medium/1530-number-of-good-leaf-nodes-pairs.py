# LeetCode 1530. Number of Good Leaf Nodes Pairs — Medium
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
# Submission 2199870159 — Accepted, Python3
#
# My thinking: each subtree hands up the
# distances of its leaves. At a node I pair
# every left leaf with every right leaf and
# count the pairs within the distance limit.

from __future__ import annotations
from typing import Optional


class Solution:
    def countPairs(self, root: Optional[TreeNode], distance: int) -> int:
        self.pairs = 0

        def dfs(node):
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [1]
            left = dfs(node.left)
            right = dfs(node.right)
            for a in left:
                for b in right:
                    if a + b <= distance:
                        self.pairs += 1
            return [d + 1 for d in left + right if d + 1 <= distance]

        dfs(root)
        return self.pairs
