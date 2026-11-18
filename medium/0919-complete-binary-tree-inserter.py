# LeetCode 919. Complete Binary Tree Inserter — Medium
# https://leetcode.com/problems/complete-binary-tree-inserter/
# Submission 2198969574 — Accepted, Python3
#
# My thinking: I keep a queue of the nodes in
# level order, starting from the first one with
# a free child spot. Each new node goes to the
# front of the queue, left first, then right.

from __future__ import annotations

from collections import deque
from typing import Optional


class CBTInserter:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        nodes = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            nodes.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        self.queue = deque(nodes)
        while self.queue[0].left and self.queue[0].right:
            self.queue.popleft()

    def insert(self, val: int) -> int:
        parent = self.queue[0]
        node = TreeNode(val)
        if not parent.left:
            parent.left = node
        else:
            parent.right = node
            self.queue.popleft()
        self.queue.append(node)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root
