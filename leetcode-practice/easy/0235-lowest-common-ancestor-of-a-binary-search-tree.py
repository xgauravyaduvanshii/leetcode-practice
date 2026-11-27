# LeetCode 235. Lowest Common Ancestor of a Binary Search Tree — Easy
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Submission 2197456453 — Accepted, Python3
#
# My thinking: in a BST the values tell me where to
# go. If both p and q are smaller than the current
# node, they are both in the left subtree. If both
# are bigger, they are both on the right. Otherwise
# the current node is the split point — that is the
# lowest common ancestor.

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        current = root
        while current:
            if p.val < current.val and q.val < current.val:
                current = current.left
            elif p.val > current.val and q.val > current.val:
                current = current.right
            else:
                return current
