# LeetCode 849. Maximize Distance to Closest Person — Medium
# https://leetcode.com/problems/maximize-distance-to-closest-person/
# Submission 2198953823 — Accepted, Python3
#
# My thinking: between two people I sit in the
# middle, half the gap away. At the ends I take
# the whole empty stretch, so I compare the
# middle gaps with both edges.

from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        best = 0
        previous = -1
        for i, seat in enumerate(seats):
            if seat == 1:
                if previous == -1:
                    best = i
                else:
                    best = max(best, (i - previous) // 2)
                previous = i
        return max(best, len(seats) - 1 - previous)
