# LeetCode 102. Binary Tree Level Order Traversal — Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Submission 2203988102 — Accepted, Python3
#
# My thinking: I walk the tree level by level with a queue,
# starting with just the root. Each pass takes every node
# currently in the queue — that is exactly one level — records
# their values, and queues up their children for the next
# pass. An empty tree has no levels, so it gives back an
# empty list.

from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result
