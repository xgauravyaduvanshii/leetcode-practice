# LeetCode 965. Univalued Binary Tree — Easy
# https://leetcode.com/problems/univalued-binary-tree/
# Submission 2197546586 — Accepted, Python3
#
# My thinking: a tree is univalued if every node has
# the same value as the root. I check each node
# against its parent as I walk down — if any child
# differs from its parent, the tree fails — and I
# do the same check for both subtrees.

class Solution:
    def isUnivalTree(self, root) -> bool:
        if not root:
            return True
        if root.left and root.left.val != root.val:
            return False
        if root.right and root.right.val != root.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
