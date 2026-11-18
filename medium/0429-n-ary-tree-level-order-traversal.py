# LeetCode 429. N-ary Tree Level Order Traversal — Medium
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/
# Submission 2198788600 — Accepted, Python3
#
# My thinking: a queue walks the tree level by
# level. I take one whole level out at a time,
# record its values, and push all of its children
# in behind it.

from collections import deque
from typing import List


class Solution:
    def levelOrder(self, root) -> List[List[int]]:
        if not root:
            return []
        levels = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            levels.append(level)
        return levels
