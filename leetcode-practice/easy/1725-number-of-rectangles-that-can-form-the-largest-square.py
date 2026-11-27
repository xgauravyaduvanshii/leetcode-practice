# LeetCode 1725. Number Of Rectangles That Can Form The Largest Square — Easy
# https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/
# Submission 2197595539 — Accepted, Python3
#
# My thinking: the biggest square a rectangle can
# make has side equal to its shorter side. I track
# the largest such side I have seen and how many
# rectangles reach it.

from typing import List


class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        best = 0
        count = 0
        for length, width in rectangles:
            side = min(length, width)
            if side > best:
                best = side
                count = 1
            elif side == best:
                count += 1
        return count
