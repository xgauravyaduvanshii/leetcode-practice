# LeetCode 2580. Count Ways to Group Overlapping Ranges — Medium
# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges/
# Submission 2205083477 — Accepted, Python3
#
# My thinking: sort by start and merge overlaps into groups —
# ranges in different groups never overlap, so each group
# independently chooses one of the two sides. That gives
# 2^(number of groups), modulo 1_000_000_007.
class Solution:
    def countWays(self, ranges: list[list[int]]) -> int:
        MOD = 1_000_000_007
        ranges.sort()
        groups = 0
        end = -1
        for s, e in ranges:
            if s > end:
                groups += 1
            end = max(end, e)
        return pow(2, groups, MOD)
