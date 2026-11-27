# LeetCode 949. Largest Time for Given Digits — Medium
# https://leetcode.com/problems/largest-time-for-given-digits/
# Submission 2198974108 — Accepted, Python3
#
# My thinking: there are only 24 ways to arrange
# four digits, so I try them all and keep the
# biggest valid time — hours under 24 and minutes
# under 60.

from itertools import permutations
from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        best = -1
        for a, b, c, d in permutations(arr):
            hours = 10 * a + b
            minutes = 10 * c + d
            if hours < 24 and minutes < 60:
                best = max(best, hours * 60 + minutes)
        if best == -1:
            return ""
        return f"{best // 60:02d}:{best % 60:02d}"
