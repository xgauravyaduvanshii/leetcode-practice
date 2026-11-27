# LeetCode 112. Path Sum — Easy
# https://leetcode.com/problems/path-sum/
# Submission 2197441268 — Accepted, Python3
#
# My thinking: I walk down from the root, subtracting
# each node's value from the target as I go. When I
# reach a leaf, the remaining target has to be exactly
# that leaf's value. If either side works, the answer
# is yes.

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining)
                or self.hasPathSum(root.right, remaining))
