# LeetCode 1936. Add Minimum Number of Rungs — Medium
# https://leetcode.com/problems/add-minimum-number-of-rungs/
# Submission 2201681119 — Accepted, Python3
#
# My thinking: every gap I cannot jump
# needs its own stepping stones — a gap
# of size g with a reach of dist needs
# (g - 1) // dist new rungs, no more.

class Solution:
    def addRungs(self, rungs: list[int], dist: int) -> int:
        ans = 0
        prev = 0
        for r in rungs:
            gap = r - prev
            if gap > dist:
                ans += (gap - 1) // dist
            prev = r
        return ans
