# LeetCode 6. Zigzag Conversion — Medium
# https://leetcode.com/problems/zigzag-conversion/
# Submission 2203755422 — Accepted, Python3

# My thinking: walk the rows top to bottom and back up, appending each
# character to its row, then join the rows. A single row returns the
# string unchanged.
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [''] * numRows
        r = 0
        step = 1
        for ch in s:
            rows[r] += ch
            if r == 0:
                step = 1
            elif r == numRows - 1:
                step = -1
            r += step
        return ''.join(rows)
