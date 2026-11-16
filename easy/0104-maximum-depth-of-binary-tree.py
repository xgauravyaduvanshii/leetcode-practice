# LeetCode 104. Maximum Depth of Binary Tree — Easy
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Submission 2197386955 — Accepted, Python3
#
# My thinking: the depth of a tree is 1 plus the deeper
# of its two children's depths. An empty tree has depth 0.

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Depth of an empty tree is 0; otherwise 1 + the deeper child's depth.
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
