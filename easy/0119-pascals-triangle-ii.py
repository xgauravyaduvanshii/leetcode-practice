# LeetCode 119. Pascal's Triangle II — Easy
# https://leetcode.com/problems/pascals-triangle-ii/
# Submission 2197442363 — Accepted, Python3
#
# My thinking: I only need one row, so I keep updating
# the same list in place. I go from right to left so
# I do not overwrite a number I still need for the
# next calculation in this row.

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            row.append(1)
            for j in range(i - 1, 0, -1):
                row[j] = row[j] + row[j - 1]
        return row
