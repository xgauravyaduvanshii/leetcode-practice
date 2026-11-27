# LeetCode 108. Convert Sorted Array to Binary Search Tree — Easy
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
# Submission 2197387561 — Accepted, Python3
#
# My thinking: the middle element makes the perfect root —
# everything smaller goes left, everything bigger goes
# right, and both sides stay balanced. I repeat the same
# step on each half until nothing is left.

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Pick the middle element as root so both sides stay balanced.
        def build(lo, hi):
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node
        return build(0, len(nums) - 1)
