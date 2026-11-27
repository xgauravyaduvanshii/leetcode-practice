# LeetCode 963. Minimum Area Rectangle II — Medium
# https://leetcode.com/problems/minimum-area-rectangle-ii/
# Submission 2198977265 — Accepted, Python3
#
# My thinking: two diagonals of a rectangle share
# their midpoint and their length. I group the
# diagonals by both, and for each pair in a group
# the area is the cross product of the two sides
# from one corner to the other's endpoints.

from collections import defaultdict
from typing import List


class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        by_mid = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                mid = (x1 + x2, y1 + y2)
                dist_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
                by_mid[(mid, dist_sq)].append(((x1, y1), (x2, y2)))
        best = float("inf")
        for diagonals in by_mid.values():
            for x in range(len(diagonals)):
                for y in range(x + 1, len(diagonals)):
                    a1, a2 = diagonals[x]
                    b1, b2 = diagonals[y]
                    area = abs((b1[0] - a1[0]) * (b2[1] - a1[1]) - (b1[1] - a1[1]) * (b2[0] - a1[0]))
                    best = min(best, area)
        return 0.0 if best == float("inf") else best
