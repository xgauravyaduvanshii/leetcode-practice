# LeetCode 1448. Count Good Nodes in Binary Tree — Medium
# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# Submission 2199853366 — Accepted, Python3
#
# My thinking: a node is good when it is at
# least as big as every ancestor above it. I
# carry the biggest value seen so far down each
# path and count the nodes that beat it.

from __future__ import annotations


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, best):
            if not node:
                return 0
            count = 1 if node.val >= best else 0
            best = max(best, node.val)
            return count + dfs(node.left, best) + dfs(node.right, best)

        return dfs(root, root.val)
