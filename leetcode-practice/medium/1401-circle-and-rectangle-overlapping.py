# LeetCode 1401. Circle and Rectangle Overlapping — Medium
# https://leetcode.com/problems/circle-and-rectangle-overlapping/
# Submission 2199049665 — Accepted, Python3
#
# My thinking: the closest point of the
# rectangle to the circle's centre decides it.
# I clamp the centre into the rectangle and
# check whether that point is within the radius.

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        closest_x = min(max(xCenter, x1), x2)
        closest_y = min(max(yCenter, y1), y2)
        return (xCenter - closest_x) ** 2 + (yCenter - closest_y) ** 2 <= radius ** 2
