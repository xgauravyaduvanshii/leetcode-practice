# LeetCode 101. Symmetric Tree — Easy
# https://leetcode.com/problems/symmetric-tree/
# Submission 2197386369 — Accepted, Python3
#
# My thinking: the tree is symmetric if its left half
# mirrors its right half. I compare the two sides
# pairwise — outer with outer, inner with inner.

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # A tree is symmetric if its left and right halves mirror each other.
        def mirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val
                    and mirror(left.left, right.right)
                    and mirror(left.right, right.left))
        return mirror(root.left, root.right) if root else True
