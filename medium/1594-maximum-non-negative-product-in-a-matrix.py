# LeetCode 1594. Maximum Non Negative Product in a Matrix — Medium
# https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/
# Submission 2199886750 — Accepted, Python3
#
# My thinking: a negative times a negative
# can become the biggest product, so each cell
# tracks both its best and its worst product
# so far. The answer is the best product at
# the end, or -1 when it is negative.

from typing import List


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        rows = len(grid)
        cols = len(grid[0])
        max_dp = [[0] * cols for _ in range(rows)]
        min_dp = [[0] * cols for _ in range(rows)]
        max_dp[0][0] = min_dp[0][0] = grid[0][0]
        for r in range(rows):
            for c in range(cols):
                if r == 0 and c == 0:
                    continue
                candidates = []
                if r > 0:
                    candidates.append(max_dp[r - 1][c] * grid[r][c])
                    candidates.append(min_dp[r - 1][c] * grid[r][c])
                if c > 0:
                    candidates.append(max_dp[r][c - 1] * grid[r][c])
                    candidates.append(min_dp[r][c - 1] * grid[r][c])
                max_dp[r][c] = max(candidates)
                min_dp[r][c] = min(candidates)
        return max_dp[rows - 1][cols - 1] % mod if max_dp[rows - 1][cols - 1] >= 0 else -1
