# LeetCode 42. Trapping Rain Water — Hard
# https://leetcode.com/problems/trapping-rain-water/
# Submission 2198365935 — Accepted, Python3
#
# My thinking: water sits on a bar only up to the
# shorter of the tallest bars on its left and right.
# I walk in from both ends with two pointers, always
# moving the shorter side, and keep the tallest bar
# seen so far on each side. When the current bar is
# shorter than that tallest bar, the gap between
# them is trapped water.

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1
        return water
