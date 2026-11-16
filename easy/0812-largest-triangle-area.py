# LeetCode 812. Largest Triangle Area — Easy
# https://leetcode.com/problems/largest-triangle-area/
# Submission 2197530884 — Accepted, Python3
#
# My thinking: there are not many points, so I can
# just try every combination of three. The area of
# a triangle from its three corners comes from the
# shoelace formula, and I keep the biggest one.

class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        best = 0.0
        n = len(points)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                for k in range(j + 1, n):
                    x3, y3 = points[k]
                    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2
                    best = max(best, area)
        return best
