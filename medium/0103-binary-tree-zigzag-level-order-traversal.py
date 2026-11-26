# LeetCode 103. Binary Tree Zigzag Level Order Traversal — Medium
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Submission 2203989946 — Accepted, Python3
#
# My thinking: I walk the tree one level at a time with a queue,
# just like a normal level-order traversal. The only extra step is
# that the direction flips after each level: even levels read
# left to right, odd levels read right to left. Instead of
# reversing the queue (which would break the children's order),
# I collect each level's values and reverse just that level's
# list when the direction is right to left. The children are
# always queued in left-to-right order, so the next level still
# comes out correctly.

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        result = []
        queue = deque([root])
        left_to_right = True
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right
        return result
