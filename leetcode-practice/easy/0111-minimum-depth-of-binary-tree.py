# LeetCode 111. Minimum Depth of Binary Tree — Easy
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Submission 2197440597 — Accepted, Python3
#
# My thinking: the depth of a leaf is 1. If a node has
# only one child, I have to go down that side — I cannot
# count the missing side as 0. If it has both children,
# I take the smaller of the two depths and add 1.

class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
