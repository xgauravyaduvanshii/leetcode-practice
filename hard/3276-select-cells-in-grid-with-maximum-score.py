# LeetCode 3276. Select Cells in Grid With Maximum Score — Hard
# https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/
# Submission 2202173448 — Accepted, Python3
#
# My thinking: each value can be taken at most
# once, from a row that contains it, and each
# row at most once. I process values largest
# first and keep a bitmask DP over which rows
# are already used: for each value I either skip
# it or take it from one of its unused rows. The
# answer is the best score over all masks.

from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        rows_for_value = {}
        for r, row in enumerate(grid):
            for v in set(row):
                rows_for_value[v] = rows_for_value.get(v, 0) | (1 << r)
        dp = [-10 ** 9] * (1 << m)
        dp[0] = 0
        for v in sorted(rows_for_value, reverse=True):
            rows = rows_for_value[v]
            ndp = dp[:]
            for mask in range(1 << m):
                cur = dp[mask]
                if cur < 0:
                    continue
                avail = rows & ~mask
                while avail:
                    lsb = avail & -avail
                    nmask = mask | lsb
                    if ndp[nmask] < cur + v:
                        ndp[nmask] = cur + v
                    avail ^= lsb
            dp = ndp
        return max(dp)
