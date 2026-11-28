# LeetCode 2482. Difference Between Ones and Zeros in Row and Column — Medium
# https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/
# Submission 2204969036 — Accepted, Python3
#
# My thinking: count the ones in each row and each column once. For
# a cell, ones minus zeros in its row is 2 * rowOnes - n, and the
# same for its column is 2 * colOnes - m, so the answer is the sum
# of the two: 2 * rowOnes + 2 * colOnes - m - n.
class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        m = len(grid)
        n = len(grid[0])
        row = [sum(r) for r in grid]
        col = [sum(grid[i][j] for i in range(m)) for j in range(n)]
        return [[2 * row[i] + 2 * col[j] - m - n for j in range(n)] for i in range(m)]
