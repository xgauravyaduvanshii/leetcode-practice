# LeetCode 1072. Flip Columns For Maximum Number of Equal Rows — Medium
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
# Submission 2198996535 — Accepted, Python3
#
# My thinking: flipping columns can only make
# two rows equal when they already match or are
# exact opposites. I normalise each row to start
# with zero, then the most common pattern is the
# answer.

from collections import Counter
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        patterns = Counter()
        for row in matrix:
            key = tuple(row) if row[0] == 0 else tuple(1 - x for x in row)
            patterns[key] += 1
        return max(patterns.values())
