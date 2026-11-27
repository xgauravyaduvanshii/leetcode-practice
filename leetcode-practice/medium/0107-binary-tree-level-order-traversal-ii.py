# LeetCode 107. Binary Tree Level Order Traversal II — Medium
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Submission 2204100547 — Accepted, Python3
#
# My thinking: this is the same level-by-level walk as ordinary
# level order traversal, only the levels come out bottom-up. So I
# walk the tree breadth-first with a queue, collecting one list of
# values per level from top to bottom, and at the end I reverse the
# list of levels. Each level's children are queued in left-to-right
# order, so the values inside every level stay in the right order,
# and reversing only flips the order of the levels themselves. An
# empty tree gives an empty answer, and a single node gives one
# level containing just that node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        if not root:
            return []
        levels = []
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
            levels.append(level)
        return levels[::-1]
