# LeetCode 106. Construct Binary Tree from Inorder and Postorder Traversal — Medium
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# Submission 2200888842 — Accepted, Python3
#
# My thinking: the last element of the postorder list is always the
# root, and in the inorder list everything left of the root belongs
# to its left subtree and everything right of it to its right
# subtree. I keep a map from value to inorder position so I can
# split the range in constant time, and I walk the postorder list
# backwards, building the right subtree before the left one, because
# postorder visits the right subtree just before the root. Each node
# is created once, so the whole build is linear.
class Solution:
    def buildTree(self, inorder, postorder):
        position = {value: i for i, value in enumerate(inorder)}
        self.next_root = len(postorder) - 1

        def build(lo, hi):
            if lo > hi:
                return None
            value = postorder[self.next_root]
            self.next_root -= 1
            node = TreeNode(value)
            node.right = build(position[value] + 1, hi)
            node.left = build(lo, position[value] - 1)
            return node

        return build(0, len(inorder) - 1)
