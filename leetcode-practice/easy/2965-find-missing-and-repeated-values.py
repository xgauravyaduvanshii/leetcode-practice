# LeetCode 2965. Find Missing and Repeated Values — Easy
# https://leetcode.com/problems/find-missing-and-repeated-values/
# Submission 2198705014 — Accepted, Python3
#
# My thinking: the grid should hold every number from
# 1 to n squared exactly once. I add everything up
# and watch for the number that appears twice — the
# gap between the expected total and the real total,
# corrected for the duplicate, is the missing number.

from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        seen = set()
        repeated = -1
        total = 0
        for row in grid:
            for value in row:
                total += value
                if value in seen:
                    repeated = value
                seen.add(value)
        expected = n * n * (n * n + 1) // 2
        return [repeated, expected - (total - repeated)]
