# LeetCode 450. Delete Node in a BST — Medium
# https://leetcode.com/problems/delete-node-in-a-bst/
# Submission 2198803824 — Accepted, Python3
#
# My thinking: I walk down to the key like a search.
# A leaf just disappears, a node with one child is
# replaced by that child, and a node with two
# children takes its successor's value — then I
# delete the successor the same way.

class Solution:
    def deleteNode(self, root, key: int):
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root
