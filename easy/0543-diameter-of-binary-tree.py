# LeetCode 543. Diameter of Binary Tree — Easy
# https://leetcode.com/problems/diameter-of-binary-tree/
# Submission 2197495562 — Accepted, Python3
#
# My thinking: the diameter is the longest path
# between any two nodes, and it passes through some
# node with its left depth on one side and its
# right depth on the other. So as I compute the
# depth of each node, I check left + right and
# remember the biggest one I see.

class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter = 0

        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.diameter
