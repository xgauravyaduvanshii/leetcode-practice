# LeetCode 84. Largest Rectangle in Histogram — Hard
# https://leetcode.com/problems/largest-rectangle-in-histogram/
# Submission 2198382465 — Accepted, Python3
#
# My thinking: I walk the bars with a stack that
# keeps their heights rising. When a shorter bar
# comes, every taller bar on the stack ends right
# here — its rectangle stretches from the bar
# after the one below it in the stack up to this
# spot. I measure each one and keep the biggest.
# A zero-height bar at the end flushes the stack.

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0
        for i, h in enumerate(heights + [0]):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] + 1 if stack else 0
                best = max(best, height * (i - left))
            stack.append(i)
        return best
