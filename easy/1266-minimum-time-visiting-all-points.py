# LeetCode 1266. Minimum Time Visiting All Points — Easy
# https://leetcode.com/problems/minimum-time-visiting-all-points/
# Submission 2197566169 — Accepted, Python3
#
# My thinking: you can move diagonally, so going from
# one point to the next costs the bigger of the
# horizontal and vertical distances — diagonal steps
# cover both at once. I add that up for every
# consecutive pair of points.

class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        total = 0
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            total += max(abs(x2 - x1), abs(y2 - y1))
        return total
