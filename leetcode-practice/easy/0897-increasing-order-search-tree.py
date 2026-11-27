# LeetCode 897. Increasing Order Search Tree — Easy
# https://leetcode.com/problems/increasing-order-search-tree/
# Submission 2197540563 — Accepted, Python3
#
# My thinking: an inorder walk of a BST visits the
# values in increasing order. So I walk inorder
# and rebuild the tree as I go — each node I visit
# becomes the right child of the previous one, with
# its left child cut off. A dummy node in front
# makes the first link easy.

class Solution:
    def increasingBST(self, root):
        dummy = TreeNode(0)
        self.cur = dummy

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            node.left = None
            self.cur.right = node
            self.cur = node
            inorder(node.right)

        inorder(root)
        return dummy.right
