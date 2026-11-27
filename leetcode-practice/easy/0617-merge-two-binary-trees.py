# LeetCode 617. Merge Two Binary Trees — Easy
# https://leetcode.com/problems/merge-two-binary-trees/
# Submission 2197505626 — Accepted, Python3
#
# My thinking: where both trees have a node, I add
# the values together. Where only one has a node, I
# just keep that side as it is. Then I do the same
# thing for the left children and the right children.

class Solution:
    def mergeTrees(self, root1, root2):
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
