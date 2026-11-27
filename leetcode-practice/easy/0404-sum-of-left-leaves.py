# LeetCode 404. Sum of Left Leaves — Easy
# https://leetcode.com/problems/sum-of-left-leaves/
# Submission 2197471836 — Accepted, Python3
#
# My thinking: I walk the whole tree. Whenever a
# node's left child is a leaf (no children of its
# own), I add its value. Everything else I just
# keep recursing into, left and right.

class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return 0
        total = 0
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        return total + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
