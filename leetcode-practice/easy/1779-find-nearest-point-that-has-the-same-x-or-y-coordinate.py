# 1779. Find Nearest Point That Has the Same X or Y Coordinate (Easy)
# https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/
# Submission 2199968260 — Accepted, Python3
from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # My thinking: only points sharing my x or my y
        # count. Among those, the nearest by Manhattan
        # distance wins, and ties go to the smallest
        # index — so I only replace the answer when a
        # point is strictly nearer.
        best_index = -1
        best_dist = float("inf")
        for i, (px, py) in enumerate(points):
            if px != x and py != y:
                continue
            dist = abs(px - x) + abs(py - y)
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return best_index
