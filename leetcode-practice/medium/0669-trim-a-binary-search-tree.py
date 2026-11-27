# LeetCode 669. Trim a Binary Search Tree — Medium
# https://leetcode.com/problems/trim-a-binary-search-tree/
# Submission 2197511755 — Accepted, Python3
#
# My thinking: I check each node against the range.
# If it is too small, the whole left side is too
# small too, so I keep only the right side. If it
# is too big, I keep only the left side. Otherwise
# the node stays, and I trim both of its children
# the same way.

class Solution:
    def trimBST(self, root, low: int, high: int):
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root
