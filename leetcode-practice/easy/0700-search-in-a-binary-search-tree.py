# LeetCode 700. Search in a Binary Search Tree — Easy
# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Submission 2197516988 — Accepted, Python3
#
# My thinking: in a BST I never need to search both
# sides. If the value I want is smaller than the
# current node, it can only be on the left; if it
# is bigger, only on the right. If I find it, I
# return that subtree; if I run out of nodes, it
# is not there.

class Solution:
    def searchBST(self, root, val: int):
        while root:
            if root.val == val:
                return root
            root = root.left if val < root.val else root.right
        return None
