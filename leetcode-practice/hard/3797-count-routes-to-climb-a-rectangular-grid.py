# LeetCode 3797. Count Routes to Climb a Rectangular Grid — Hard
# https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/
# Submission 2203183536 — Accepted, Python3
import math

import numpy as np
from typing import List


class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        # My thinking: a route climbs from the bottom row to the
        # top row, each step moving up one row or sideways within
        # a row, never sideways twice in a row, and every step
        # has Euclidean length at most d. Work top-down with two
        # states per cell: free (arrived from below, or the
        # start) may end here on the top row, move up, or move
        # sideways; stay (just moved sideways) may only move up
        # or end on the top row. An up step reaches columns
        # within isqrt(d^2 - 1) and a sideways step columns
        # within d, so both transitions are range sums over the
        # row above (for up) or the current row's stay values
        # (for sideways) — prefix sums make each row O(m) with
        # numpy. The answer is the sum of free over the bottom
        # row, all modulo 1e9 + 7.
        MOD = 10 ** 9 + 7
        n = len(grid)
        m = len(grid[0])
        avail = np.array([[ch == "." for ch in row] for row in grid], dtype=bool)
        up_reach = math.isqrt(d * d - 1)
        cols = np.arange(m)

        def range_sums(pref, reach):
            # pref is the prefix sums of a row (length m + 1);
            # return, for every column c, the sum over
            # [c - reach, c + reach] clipped to the row.
            lo = np.maximum(0, cols - reach)
            hi = np.minimum(m - 1, cols + reach)
            return pref[hi + 1] - pref[lo]

        free_prev = np.zeros(m, dtype=np.int64)
        for r in range(n):
            row_avail = avail[r]
            if r == 0:
                # No row above: arriving sideways is the only way
                # in, and a route may simply end on the top row.
                stay = np.where(row_avail, 1, 0).astype(np.int64)
            else:
                pref_up = np.concatenate(([0], np.cumsum(free_prev) % MOD))
                stay = np.where(row_avail, range_sums(pref_up, up_reach), 0) % MOD
            pref_stay = np.concatenate(([0], np.cumsum(stay) % MOD))
            side = (range_sums(pref_stay, d) - stay) % MOD
            if r == 0:
                free = np.where(row_avail, (1 + side) % MOD, 0)
            else:
                free = np.where(row_avail, (range_sums(pref_up, up_reach) + side) % MOD, 0)
            free_prev = free
        return int(free_prev.sum() % MOD)
