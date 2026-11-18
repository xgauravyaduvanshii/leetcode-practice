# LeetCode 236. Lowest Common Ancestor of a Binary Tree — Medium
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Submission 2198723449 — Accepted, Python3
#
# My thinking: I search down from the root. If I
# find p in one side and q in the other, this node
# is where their paths split, so it is the answer.
# If only one side finds anything, the answer is
# whatever that side found.

from typing import Optional


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None or root is p or root is q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
