# LeetCode 2236. Root Equals Sum of Children — Easy
# https://leetcode.com/problems/root-equals-sum-of-children/
# Submission 2197619262 — Accepted, Python3
#
# My thinking: I just check whether the root's value
# equals the sum of its two children's values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: TreeNode | None) -> bool:
        return root.val == root.left.val + root.right.val
