# LeetCode 2541. Minimum Operations to Make Array Equal II — Medium
# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/
# Submission 2205056142 — Accepted, Python3
#
# My thinking: one operation moves k units from one element to
# another, so the total sum never changes. Each position's gap
# must be a multiple of k, and the total units that must go up
# must equal the total that must come down; that total is the
# answer. k = 0 means the arrays must already match.
class Solution:
    def minOperations(self, nums1: list[int], nums2: list[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        up = down = 0
        for a, b in zip(nums1, nums2):
            d = b - a
            if d % k:
                return -1
            if d > 0:
                up += d // k
            else:
                down += (-d) // k
        return up if up == down else -1
