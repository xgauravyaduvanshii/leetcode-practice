# LeetCode 894. All Possible Full Binary Trees — Medium
# https://leetcode.com/problems/all-possible-full-binary-trees/
# Submission 2198965266 — Accepted, Python3
#
# My thinking: a full binary tree with n nodes
# has a root plus two full subtrees whose sizes
# add to n minus one, both odd. I try every
# split and combine every left tree with every
# right tree.

from __future__ import annotations

from typing import List, Optional


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        trees = []
        for left_count in range(1, n, 2):
            right_count = n - 1 - left_count
            for left in self.allPossibleFBT(left_count):
                for right in self.allPossibleFBT(right_count):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    trees.append(root)
        return trees
