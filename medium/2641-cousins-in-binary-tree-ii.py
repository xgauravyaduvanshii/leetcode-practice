# LeetCode 2641. Cousins in Binary Tree II — Medium
# https://leetcode.com/problems/cousins-in-binary-tree-ii/
# Submission 2205108574 — Accepted, Python3
#
# My thinking: a node's new value is its level total minus
# its own sibling group. Collect every level's sum and its
# nodes first (all from original values), then walk the levels
# in order, giving each child the level sum minus the sum of
# its parent's children.
from collections import deque


class Solution:
    def replaceValueInTree(self, root):
        q = deque([root])
        level_sums = []
        levels = []
        while q:
            s = 0
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                s += node.val
                level.append(node)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level_sums.append(s)
            levels.append(level)
        root.val = 0
        for d, level in enumerate(levels):
            for node in level:
                sib = 0
                if node.left:
                    sib += node.left.val
                if node.right:
                    sib += node.right.val
                if node.left:
                    node.left.val = level_sums[d + 1] - sib
                if node.right:
                    node.right.val = level_sums[d + 1] - sib
        return root
