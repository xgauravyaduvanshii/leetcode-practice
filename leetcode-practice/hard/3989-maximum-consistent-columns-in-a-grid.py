# LeetCode 3989. Maximum Consistent Columns in a Grid — Hard
# https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/
# Submission 2203499116 — Accepted, Python3
from typing import List


class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        # My thinking: the kept columns keep their order,
        # so this is a longest-subsequence problem over
        # columns: dp[j] is the longest consistent run
        # ending at column j, and i can precede j exactly
        # when every row differs by at most limit between
        # the two columns. Checking a pair costs O(m) with
        # an early break on the first row that violates
        # the limit, so the whole DP is O(n^2 * m) with
        # n, m <= 250. A single column is always
        # consistent, so dp starts at 1.
        n = len(grid[0])
        cols = list(zip(*grid))
        dp = [1] * n
        for j in range(n):
            cj = cols[j]
            best = 1
            for i in range(j):
                ci = cols[i]
                ok = True
                for a, b in zip(ci, cj):
                    if abs(a - b) > limit:
                        ok = False
                        break
                if ok and dp[i] + 1 > best:
                    best = dp[i] + 1
            dp[j] = best
        return max(dp)
