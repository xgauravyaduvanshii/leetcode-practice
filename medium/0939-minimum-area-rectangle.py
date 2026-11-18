# LeetCode 939. Minimum Area Rectangle — Medium
# https://leetcode.com/problems/minimum-area-rectangle/
# Submission 2198973027 — Accepted, Python3
#
# My thinking: a rectangle needs two x-columns
# sharing two y-values. I group the points by
# column, then check every pair of columns for
# shared heights and keep the smallest area.

from collections import defaultdict
from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        by_x = defaultdict(set)
        for x, y in points:
            by_x[x].add(y)
        best = float("inf")
        xs = sorted(by_x)
        for i in range(len(xs)):
            for j in range(i + 1, len(xs)):
                common = by_x[xs[i]] & by_x[xs[j]]
                if len(common) < 2:
                    continue
                ys = sorted(common)
                for k in range(len(ys) - 1):
                    area = (xs[j] - xs[i]) * (ys[k + 1] - ys[k])
                    best = min(best, area)
        return 0 if best == float("inf") else best
