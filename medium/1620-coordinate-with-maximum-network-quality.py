# LeetCode 1620. Coordinate With Maximum Network Quality — Medium
# https://leetcode.com/problems/coordinate-with-maximum-network-quality/
# Submission 2199893564 — Accepted, Python3
#
# My thinking: the best point is always near
# a tower, and the grid is small. I score
# every integer point by adding each tower's
# signal — floor of quality over one plus
# distance — and keep the best, breaking ties
# toward the smaller coordinates.

from typing import List


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        best_quality = -1
        best_point = [0, 0]
        for x in range(51):
            for y in range(51):
                quality = 0
                for tx, ty, q in towers:
                    dist = ((tx - x) ** 2 + (ty - y) ** 2) ** 0.5
                    if dist <= radius:
                        quality += int(q / (1 + dist))
                if quality > best_quality:
                    best_quality = quality
                    best_point = [x, y]
        return best_point
