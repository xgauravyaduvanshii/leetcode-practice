# LeetCode 2415. Reverse Odd Levels of Binary Tree — Medium
# https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/
# Submission 2204795798 — Accepted, Python3
#
# My thinking: BFS level by level, collecting each level's nodes. On
# odd levels (1, 3, 5, ...) the values are written back in reverse
# order, which swaps symmetric nodes' values; even levels and the tree
# structure stay untouched.
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        q = deque([root])
        level = 0
        while q:
            n = len(q)
            nodes = []
            for _ in range(n):
                node = q.popleft()
                nodes.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if level % 2 == 1:
                vals = [node.val for node in nodes][::-1]
                for node, v in zip(nodes, vals):
                    node.val = v
            level += 1
        return root
