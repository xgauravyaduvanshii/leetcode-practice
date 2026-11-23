# LeetCode 1953. Maximum Number of Weeks for Which You Can Work — Medium
# https://leetcode.com/problems/maximum-number-of-weeks-for-which-you-can-work/
# Submission 2201845907 — Accepted, Python3
#
# My thinking: the busiest project can
# only be worked on when another project
# fills the week between its milestones,
# so if it outnumbers all the rest put
# together it caps the run, and otherwise
# every milestone gets done.

class Solution:
    def numberOfWeeks(self, milestones: list[int]) -> int:
        total = sum(milestones)
        mx = max(milestones)
        rest = total - mx
        if mx <= rest + 1:
            return total
        return 2 * rest + 1
