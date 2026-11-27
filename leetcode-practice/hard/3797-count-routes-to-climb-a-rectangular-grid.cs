// LeetCode 3797. Count Routes to Climb a Rectangular Grid — Hard
// https://leetcode.com/problems/count-routes-to-climb-a-rectangular-grid/
// Submission 2203184132 — Accepted, C#
using System;

public class Solution {
    public int NumberOfRoutes(string[] grid, int d) {
        // My thinking: a route climbs from the bottom row to the
        // top row, each step moving up one row or sideways within
        // a row, never sideways twice in a row, and every step
        // has Euclidean length at most d. Work top-down with two
        // states per cell: free (arrived from below, or the
        // start) may end here on the top row, move up, or move
        // sideways; stay (just moved sideways) may only move up
        // or end on the top row. An up step reaches columns
        // within isqrt(d^2 - 1) and a sideways step columns
        // within d, so both transitions are range sums over the
        // row above (for up) or the current row's stay values
        // (for sideways) — prefix sums make each row O(m). The
        // answer is the sum of free over the bottom row, all
        // modulo 1e9 + 7.
        const int MOD = 1000000007;
        int n = grid.Length;
        int m = grid[0].Length;
        int upReach = (int)Math.Sqrt(d * d - 1);
        while ((upReach + 1) * (upReach + 1) <= d * d - 1) upReach++;
        while (upReach * upReach > d * d - 1) upReach--;

        long RangeSum(long[] pref, int c, int reach) {
            int lo = Math.Max(0, c - reach);
            int hi = Math.Min(m - 1, c + reach);
            return (pref[hi + 1] - pref[lo] + MOD) % MOD;
        }

        long[] freePrev = new long[m];
        long[] stay = new long[m];
        long[] free = new long[m];
        long[] prefUp = new long[m + 1];
        long[] prefStay = new long[m + 1];
        for (int r = 0; r < n; r++) {
            if (r == 0) {
                // No row above: arriving sideways is the only way
                // in, and a route may simply end on the top row.
                for (int c = 0; c < m; c++) stay[c] = grid[r][c] == '.' ? 1 : 0;
            } else {
                prefUp[0] = 0;
                for (int c = 0; c < m; c++) prefUp[c + 1] = (prefUp[c] + freePrev[c]) % MOD;
                for (int c = 0; c < m; c++) {
                    stay[c] = grid[r][c] == '.' ? RangeSum(prefUp, c, upReach) : 0;
                }
            }
            prefStay[0] = 0;
            for (int c = 0; c < m; c++) prefStay[c + 1] = (prefStay[c] + stay[c]) % MOD;
            for (int c = 0; c < m; c++) {
                if (grid[r][c] != '.') {
                    free[c] = 0;
                    continue;
                }
                long side = (RangeSum(prefStay, c, d) - stay[c] + MOD) % MOD;
                if (r == 0) {
                    free[c] = (1 + side) % MOD;
                } else {
                    free[c] = (RangeSum(prefUp, c, upReach) + side) % MOD;
                }
            }
            Array.Copy(free, freePrev, m);
        }
        long ans = 0;
        for (int c = 0; c < m; c++) ans = (ans + freePrev[c]) % MOD;
        return (int)ans;
    }
}
