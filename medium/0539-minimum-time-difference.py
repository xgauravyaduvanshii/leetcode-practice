# LeetCode 539. Minimum Time Difference — Medium
# https://leetcode.com/problems/minimum-time-difference/
# Submission 2198859133 — Accepted, Python3
#
# My thinking: once the times are sorted, the
# smallest gap is between two neighbours — except
# for the gap that wraps past midnight, which I
# check separately.

from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = sorted(int(t[:2]) * 60 + int(t[3:]) for t in timePoints)
        best = 24 * 60
        for i in range(1, len(minutes)):
            best = min(best, minutes[i] - minutes[i - 1])
        best = min(best, minutes[0] + 24 * 60 - minutes[-1])
        return best
