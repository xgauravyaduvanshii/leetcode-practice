# LeetCode 1413. Minimum Value to Get Positive Step by Step Sum — Easy
# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
# Submission 2197576881 — Accepted, Python3
#
# My thinking: as I walk through the numbers I track
# the running total and the lowest it ever dips.
# The starting value has to be big enough to lift
# that lowest dip up to at least 1, so the answer
# is 1 minus the minimum prefix sum.

class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        min_prefix = 0
        prefix = 0
        for num in nums:
            prefix += num
            min_prefix = min(min_prefix, prefix)
        return 1 - min_prefix
