# LeetCode 240. Search a 2D Matrix II — Medium
# https://leetcode.com/problems/search-a-2d-matrix-ii/
# Submission 2198725189 — Accepted, Python3
#
# My thinking: I start at the top-right corner,
# where the row grows to the left and the column
# grows downward. If the value is too big I move
# left, if it is too small I move down — each step
# throws away a whole row or column, so I walk at
# most one row and one column.

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            value = matrix[row][col]
            if value == target:
                return True
            if value > target:
                col -= 1
            else:
                row += 1
        return False
