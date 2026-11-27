# LeetCode 1232. Check If It Is a Straight Line — Easy
# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# Submission 2197564137 — Accepted, Python3
#
# My thinking: all points lie on one line if every
# point has the same slope from the first point.
# To avoid dividing (and floating-point trouble), I
# compare cross products — the direction from the
# first point to each point must match the
# direction to the second point.

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for x, y in coordinates[2:]:
            if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
                return False
        return True
