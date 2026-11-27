# LeetCode 221. Maximal Square — Medium
# https://leetcode.com/problems/maximal-square/
# Submission 2198458172 — Accepted, Python3
#
# My thinking: for each cell I ask how big a square
# of 1s ends at that cell. If the cell is a 1, the
# square is one bigger than the smallest of the
# three squares ending above it, to its left, and
# diagonally above-left — because all three must
# extend together. The biggest square I find,
# squared, is the answer.

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        best = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    best = max(best, dp[i][j])
        return best * best
