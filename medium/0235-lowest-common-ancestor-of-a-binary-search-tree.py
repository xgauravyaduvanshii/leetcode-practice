# LeetCode 235. Lowest Common Ancestor of a Binary Search Tree — Medium
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Submission 2198464710 — Accepted, Python3
#
# My thinking: in a BST, both numbers sit on the
# same side of any ancestor that is not their
# lowest common one — if both are smaller I go
# left, if both are bigger I go right. The first
# node where they split, or one of the numbers
# itself, is the lowest common ancestor.

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
        return None
