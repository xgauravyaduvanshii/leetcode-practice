# LeetCode 452. Minimum Number of Arrows to Burst Balloons — Medium
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
# Submission 2198804982 — Accepted, Python3
#
# My thinking: sorting by the right end and always
# shooting at the earliest ending balloon hits every
# balloon that overlaps it. A balloon starting past
# that shot needs a new arrow.

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[1])
        arrows = 0
        end = float("-inf")
        for start, finish in points:
            if start > end:
                arrows += 1
                end = finish
        return arrows
