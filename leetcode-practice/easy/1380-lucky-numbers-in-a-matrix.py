# LeetCode 1380. Lucky Numbers in a Matrix — Easy
# https://leetcode.com/problems/lucky-numbers-in-a-matrix/
# Submission 2197574744 — Accepted, Python3
#
# My thinking: a lucky number is the smallest in its
# row and the largest in its column. I take each
# row's minimum, find its column, and check whether
# every number in that column is no bigger than it.
# If so, it is lucky.

class Solution:
    def luckyNumbers(self, matrix: list[list[int]]) -> list[int]:
        result = []
        for row in matrix:
            min_val = min(row)
            j = row.index(min_val)
            if all(matrix[r][j] <= min_val for r in range(len(matrix))):
                result.append(min_val)
        return result
