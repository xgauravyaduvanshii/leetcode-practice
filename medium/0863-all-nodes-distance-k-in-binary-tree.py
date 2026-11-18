# LeetCode 863. All Nodes Distance K in Binary Tree — Medium
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Submission 2198957230 — Accepted, Python3
#
# My thinking: I first record every node's
# parent, so the tree can be walked in all
# directions. Then a breadth-first search from
# the target collects every node exactly k steps
# away.

from __future__ import annotations

from collections import deque
from typing import List


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def walk(node, par=None):
            if not node:
                return
            parent[node] = par
            walk(node.left, node)
            walk(node.right, node)

        walk(root)
        result = []
        queue = deque([(target, 0)])
        seen = {target}
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                result.append(node.val)
                continue
            for nxt in (node.left, node.right, parent[node]):
                if nxt and nxt not in seen:
                    seen.add(nxt)
                    queue.append((nxt, dist + 1))
        return result
