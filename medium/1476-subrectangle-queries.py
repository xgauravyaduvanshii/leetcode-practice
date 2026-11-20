# LeetCode 1476. Subrectangle Queries — Medium
# https://leetcode.com/problems/subrectangle-queries/
# Submission 2199857909 — Accepted, Python3
#
# My thinking: the rectangle is small enough
# to update directly. An update paints every
# cell in the range; a query just reads one
# cell back.

from typing import List


class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.rectangle[r][c] = newValue

    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
