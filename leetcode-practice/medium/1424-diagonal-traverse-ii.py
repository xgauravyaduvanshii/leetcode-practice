# LeetCode 1424. Diagonal Traverse II — Medium
# https://leetcode.com/problems/diagonal-traverse-ii/
# Submission 2199056538 — Accepted, Python3
#
# My thinking: cells on one diagonal share the
# same row-plus-column sum. I gather them in
# that order and read each diagonal back from
# the bottom up.

from collections import defaultdict
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        for r, row in enumerate(nums):
            for c, value in enumerate(row):
                diagonals[r + c].append(value)
        result = []
        for key in sorted(diagonals):
            result.extend(reversed(diagonals[key]))
        return result
