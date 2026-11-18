# LeetCode 223. Rectangle Area — Medium
# https://leetcode.com/problems/rectangle-area/
# Submission 2198460181 — Accepted, Python3
#
# My thinking: the total area is the two rectangles
# added together, minus the part where they overlap
# — counted twice otherwise. The overlap's width
# is how far the right edge of the left rectangle
# reaches past the left edge of the right one, and
# likewise for its height; if they do not overlap
# at all, that part is zero.

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        overlap_w = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_h = max(0, min(ay2, by2) - max(ay1, by1))
        return area_a + area_b - overlap_w * overlap_h
