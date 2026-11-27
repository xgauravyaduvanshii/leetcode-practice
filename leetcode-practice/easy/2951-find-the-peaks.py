# LeetCode 2951. Find the Peaks — Easy
# https://leetcode.com/problems/find-the-peaks/
# Submission 2198703831 — Accepted, Python3
#
# My thinking: a peak is an element bigger than both
# of its neighbours, so I scan the inside of the
# array and keep the positions that qualify.

from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [
            i
            for i in range(1, len(mountain) - 1)
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]
        ]
