# LeetCode 1637. Widest Vertical Area Between Two Points Containing No Points — Easy
# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/
# Submission 2197591163 — Accepted, Python3
#
# My thinking: a vertical strip is bounded by two
# x-coordinates, so only the x values matter. I
# sort them and take the biggest gap between two
# neighbours — that is the widest empty strip.

class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        xs = sorted(p[0] for p in points)
        return max(xs[i + 1] - xs[i] for i in range(len(xs) - 1))
