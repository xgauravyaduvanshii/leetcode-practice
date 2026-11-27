# LeetCode 391. Perfect Rectangle — Hard
# https://leetcode.com/problems/perfect-rectangle/
# Submission 2198409485 — Accepted, Python3
#
# My thinking: the small rectangles must add up to
# exactly the area of the big rectangle they claim
# to cover. Then I count every corner: the four
# corners of the big rectangle must appear exactly
# once, and every other corner must appear an even
# number of times — an odd count would mean a gap
# or an overlap there.

from typing import List


class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corners = {}
        area = 0
        min_x = min_y = float("inf")
        max_x = max_y = float("-inf")
        for x1, y1, x2, y2 in rectangles:
            area += (x2 - x1) * (y2 - y1)
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)
            for corner in ((x1, y1), (x1, y2), (x2, y1), (x2, y2)):
                corners[corner] = corners.get(corner, 0) + 1
        if area != (max_x - min_x) * (max_y - min_y):
            return False
        outer = {(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)}
        for corner, count in corners.items():
            if corner in outer:
                if count != 1:
                    return False
            elif count % 2 != 0:
                return False
        return True
