# LeetCode 1288. Remove Covered Intervals — Medium
# https://leetcode.com/problems/remove-covered-intervals/
# Submission 2199023764 — Accepted, Python3
#
# My thinking: I sort by start, longest first
# when starts tie. An interval survives only
# when it reaches farther than every interval
# before it — anything shorter is covered.

from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        remaining = 0
        farthest = -1
        for start, end in intervals:
            if end > farthest:
                remaining += 1
                farthest = end
        return remaining
