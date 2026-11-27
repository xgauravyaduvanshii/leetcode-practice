# LeetCode 435. Non-overlapping Intervals — Medium
# https://leetcode.com/problems/non-overlapping-intervals/
# Submission 2198793610 — Accepted, Python3
#
# My thinking: sorting by end time and always
# keeping the interval that finishes first leaves
# the most room for the rest. An interval that
# starts before the last kept one ends has to go.

from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        removed = 0
        end = float("-inf")
        for start, finish in intervals:
            if start >= end:
                end = finish
            else:
                removed += 1
        return removed
