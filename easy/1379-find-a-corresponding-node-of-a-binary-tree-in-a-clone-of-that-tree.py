# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree (Easy)
# https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
# Submission 2199968035 — Accepted, Python3
from __future__ import annotations

from typing import Optional


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        # My thinking: walk the original tree and its
        # clone side by side. The moment the walk in the
        # original reaches the target, the matching node
        # in the clone is the answer.
        if original is None:
            return None
        if original is target:
            return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left is not None:
            return left
        return self.getTargetCopy(original.right, cloned.right, target)
