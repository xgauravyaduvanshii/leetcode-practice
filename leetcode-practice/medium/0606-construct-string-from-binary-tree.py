# LeetCode 606. Construct String from Binary Tree — Medium
# https://leetcode.com/problems/construct-string-from-binary-tree/
# Submission 2197505067 — Accepted, Python3
#
# My thinking: I write the node's value, then its
# children in brackets. If there is a right child,
# the left child's brackets have to be there even
# when the left child is missing, so the string
# still shows the shape. If there is no left or
# right child, there are no brackets at all.

class Solution:
    def tree2str(self, root) -> str:
        if not root:
            return ""
        result = str(root.val)
        if root.left or root.right:
            result += "(" + self.tree2str(root.left) + ")"
        if root.right:
            result += "(" + self.tree2str(root.right) + ")"
        return result
