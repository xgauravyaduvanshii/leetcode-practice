# LeetCode 1848. Minimum Distance to the Target Element — Easy
# https://leetcode.com/problems/minimum-distance-to-the-target-element/
# Submission 2197601307 — Accepted, Python3
#
# My thinking: I look at every position that holds
# the target and measure how far it is from start.
# The smallest distance wins.

class Solution:
    def getMinDistance(self, nums: list[int], target: int, start: int) -> int:
        return min(abs(i - start) for i, x in enumerate(nums) if x == target)
