# LeetCode 978. Longest Turbulent Subarray — Medium
# https://leetcode.com/problems/longest-turbulent-subarray/
# Submission 2198980030 — Accepted, Python3
#
# My thinking: I track how long the current run
# is when it ends going up, and when it ends
# going down. Each new step extends the run that
# came from the opposite direction, and equal
# neighbours restart both at one.

from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        best = 1
        up = down = 1
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                up = down + 1
                down = 1
            elif arr[i] < arr[i - 1]:
                down = up + 1
                up = 1
            else:
                up = down = 1
            best = max(best, up, down)
        return best
