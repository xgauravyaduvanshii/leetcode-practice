# LeetCode 1037. Valid Boomerang — Easy
# https://leetcode.com/problems/valid-boomerang/
# Submission 2197553646 — Accepted, Python3
#
# My thinking: three points make a boomerang if they
# are not on one straight line. Two lines from the
# first point to the other two have the same slope
# only if the cross products are equal — so if the
# cross products differ, the points are not
# collinear.

class Solution:
    def isBoomerang(self, points: list[list[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]
        return (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1)
