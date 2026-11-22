# LeetCode 11. Container With Most Water — Medium
# https://leetcode.com/problems/container-with-most-water/
# Submission 2200941370 — Accepted, Python3
#
# My thinking: I start with the two ends, because any
# container with a shorter side cannot beat the current
# one, and I keep moving the shorter side inward.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        best = 0
        while left < right:
            best = max(best, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return best
