# LeetCode 226. Invert Binary Tree — Easy
# https://leetcode.com/problems/invert-binary-tree/
# Submission 2197454291 — Accepted, Python3
#
# My thinking: to invert a tree I swap the left and
# right child of every node, and do the same thing
# for each child. The swap happens first, then I
# recurse down both sides.

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
