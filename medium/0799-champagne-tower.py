# LeetCode 799. Champagne Tower — Medium
# https://leetcode.com/problems/champagne-tower/
# Submission 2198942557 — Accepted, Python3
#
# My thinking: I pour row by row. A glass keeps
# one unit and splits the rest evenly between the
# two glasses below it, so I only need the row I
# am pouring from.

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        row = [float(poured)]
        for _ in range(query_row):
            next_row = [0.0] * (len(row) + 1)
            for i, amount in enumerate(row):
                overflow = max(0.0, amount - 1) / 2
                next_row[i] += overflow
                next_row[i + 1] += overflow
            row = next_row
        return min(1.0, row[query_glass])
