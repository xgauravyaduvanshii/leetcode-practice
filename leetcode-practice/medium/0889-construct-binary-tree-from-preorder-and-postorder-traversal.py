# LeetCode 889. Construct Binary Tree from Preorder and Postorder Traversal — Medium
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
# Submission 2198962849 — Accepted, Python3
#
# My thinking: the first preorder value is the
# root, and the second is the left child's root.
# Where that value sits in the postorder tells me
# where the left subtree ends, so I split both
# lists there and build each side the same way.

from __future__ import annotations

from typing import List, Optional


class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        left_root = preorder[1]
        split = postorder.index(left_root)
        root.left = self.constructFromPrePost(preorder[1:split + 2], postorder[:split + 1])
        root.right = self.constructFromPrePost(preorder[split + 2:], postorder[split + 1:-1])
        return root
