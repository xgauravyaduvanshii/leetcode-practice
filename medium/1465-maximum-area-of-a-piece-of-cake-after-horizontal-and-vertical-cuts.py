# LeetCode 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts — Medium
# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
# Submission 2199856701 — Accepted, Python3
#
# My thinking: the biggest piece comes from
# the widest gap between two cuts — or between
# a cut and an edge — in each direction. I
# multiply the two widest gaps.

from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        max_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i - 1])
        max_w = max(verticalCuts[0], w - verticalCuts[-1])
        for i in range(1, len(verticalCuts)):
            max_w = max(max_w, verticalCuts[i] - verticalCuts[i - 1])
        return (max_h * max_w) % (10 ** 9 + 7)
