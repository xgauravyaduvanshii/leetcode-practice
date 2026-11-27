# LeetCode 2397. Maximum Rows Covered by Columns — Medium
# https://leetcode.com/problems/maximum-rows-covered-by-columns/
# Submission 2204780265 — Accepted, Python3
#
# My thinking: there are at most 12 columns, so I can try every subset
# of exactly numSelect columns (each row is a bitmask of its 1s). A row
# is covered when all its 1-columns are selected, i.e. row & ~sel == 0.
# The best subset's covered-row count is the answer.
class Solution:
    def maximumRows(self, matrix: list[list[int]], numSelect: int) -> int:
        n = len(matrix[0])
        rows = []
        for row in matrix:
            mask = 0
            for j, v in enumerate(row):
                if v:
                    mask |= 1 << j
            rows.append(mask)
        best = 0
        for sel in range(1 << n):
            if bin(sel).count('1') != numSelect:
                continue
            covered = 0
            for r in rows:
                if r & ~sel == 0:
                    covered += 1
            if covered > best:
                best = covered
        return best
