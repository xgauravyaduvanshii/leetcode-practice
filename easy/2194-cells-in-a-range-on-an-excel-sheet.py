# LeetCode 2194. Cells in a Range on an Excel Sheet — Easy
# https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/
# Submission 2197617129 — Accepted, Python3
#
# My thinking: the range gives me the start and end
# columns and rows. I loop over every column from
# the first to the last, and inside that every row,
# and write out each cell name.

class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        c1, r1, _, c2, r2 = s
        return [f"{chr(c)}{r}" for c in range(ord(c1), ord(c2) + 1) for r in range(int(r1), int(r2) + 1)]
