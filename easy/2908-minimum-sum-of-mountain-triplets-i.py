# LeetCode 2908. Minimum Sum of Mountain Triplets I — Easy
# https://leetcode.com/problems/minimum-sum-of-mountain-triplets-i/
# Submission 2198695136 — Accepted, Python3
#
# My thinking: for each middle position I take the
# smallest smaller number to its left and the
# smallest smaller number to its right. If both exist
# they make the cheapest mountain with that peak, and
# the best peak overall is the answer.

from typing import List


class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        best = float("inf")
        n = len(nums)
        for j in range(1, n - 1):
            left = min((nums[i] for i in range(j) if nums[i] < nums[j]), default=None)
            right = min(
                (nums[k] for k in range(j + 1, n) if nums[k] < nums[j]), default=None
            )
            if left is not None and right is not None:
                best = min(best, left + nums[j] + right)
        return -1 if best == float("inf") else best
