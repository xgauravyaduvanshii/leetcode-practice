# LeetCode 572. Subtree of Another Tree — Easy
# https://leetcode.com/problems/subtree-of-another-tree/
# Submission 2197500560 — Accepted, Python3
#
# My thinking: I check every node of the big tree —
# is the smaller tree the same as the tree starting
# here? "Same" means the same values and the same
# shape, all the way down. If no node matches, it
# is not a subtree.

class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not root:
            return False
        if self.isSame(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSame(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        return a.val == b.val and self.isSame(a.left, b.left) and self.isSame(a.right, b.right)
