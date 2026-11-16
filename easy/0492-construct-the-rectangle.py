# LeetCode 492. Construct the Rectangle — Easy
# https://leetcode.com/problems/construct-the-rectangle/
# Submission 2197483956 — Accepted, Python3
#
# My thinking: I need length >= width, both multiply
# to the area, and as close together as possible.
# So I start at the square root and walk down until
# I find a width that divides the area evenly.

class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        w = int(area ** 0.5)
        while area % w != 0:
            w -= 1
        return [area // w, w]
