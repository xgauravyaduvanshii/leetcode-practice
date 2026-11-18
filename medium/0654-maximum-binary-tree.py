# LeetCode 654. Maximum Binary Tree — Medium
# https://leetcode.com/problems/maximum-binary-tree/
# Submission 2198899668 — Accepted, Python3
#
# My thinking: the biggest number becomes the root,
# everything to its left builds the left subtree
# and everything to its right builds the right one
# — the same rule, applied again and again.

from __future__ import annotations

from typing import List, Optional


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        pivot = nums.index(max(nums))
        return TreeNode(
            nums[pivot],
            self.constructMaximumBinaryTree(nums[:pivot]),
            self.constructMaximumBinaryTree(nums[pivot + 1:]),
        )
