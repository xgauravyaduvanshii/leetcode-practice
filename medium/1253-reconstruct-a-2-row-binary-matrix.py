# LeetCode 1253. Reconstruct a 2-Row Binary Matrix — Medium
# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/
# Submission 2199018602 — Accepted, Python3
#
# My thinking: columns summing to two fill both
# rows at once. For the rest I give each single
# one to the row that still needs more, and the
# answer is impossible when a row ends up short
# or over.

from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        top = [0] * len(colsum)
        bottom = [0] * len(colsum)
        for i, value in enumerate(colsum):
            if value == 2:
                top[i] = bottom[i] = 1
                upper -= 1
                lower -= 1
            elif value == 1:
                if upper > lower:
                    top[i] = 1
                    upper -= 1
                else:
                    bottom[i] = 1
                    lower -= 1
        if upper != 0 or lower != 0:
            return []
        return [top, bottom]
