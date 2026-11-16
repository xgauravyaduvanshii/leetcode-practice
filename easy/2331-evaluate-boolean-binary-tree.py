# LeetCode 2331. Evaluate Boolean Binary Tree — Easy
# https://leetcode.com/problems/evaluate-boolean-binary-tree/
# Submission 2197623308 — Accepted, Python3
#
# My thinking: a leaf holds 0 or 1, and an internal
# node holds 2 for OR or 3 for AND. I evaluate the
# tree recursively — leaves give their value, and
# each parent combines its children's results.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: TreeNode | None) -> bool:
        if root.left is None and root.right is None:
            return root.val == 1
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        if root.val == 2:
            return left or right
        return left and right
