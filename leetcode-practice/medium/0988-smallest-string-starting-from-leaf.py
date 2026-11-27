# LeetCode 988. Smallest String Starting From Leaf — Medium
# https://leetcode.com/problems/smallest-string-starting-from-leaf/
# Submission 2198982519 — Accepted, Python3
#
# My thinking: I walk every root-to-leaf path
# and read the letters backwards, from the leaf
# up. The smallest of those strings is the
# answer.

from __future__ import annotations

from typing import Optional


class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        best = []

        def walk(node, path):
            if not node:
                return
            path.append(chr(ord("a") + node.val))
            if not node.left and not node.right:
                candidate = "".join(reversed(path))
                if not best or candidate < best[0]:
                    best.clear()
                    best.append(candidate)
            walk(node.left, path)
            walk(node.right, path)
            path.pop()

        walk(root, [])
        return best[0]
