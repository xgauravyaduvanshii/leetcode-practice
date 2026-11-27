// LeetCode 2435. Paths in Matrix Whose Sum Is Divisible by K — Hard
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/
// Submission 2201740544 — Accepted, C#
//
// My thinking: only the remainder of the
// running sum matters — I carry, for each
// cell, how many ways reach it with each
// remainder, and pass them down and right.

using System;

public class Solution {
    private const int MOD = 1000000007;
    public int NumberOfPaths(int[][] grid, int k) {
        int m = grid.Length, n = grid[0].Length;
        int[,,] dp = new int[m, n, k];
        dp[0, 0, grid[0][0] % k] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                int v = grid[i][j] % k;
                for (int r = 0; r < k; r++) {
                    long ways = 0;
                    if (i > 0) ways += dp[i - 1, j, (r - v + k) % k];
                    if (j > 0) ways += dp[i, j - 1, (r - v + k) % k];
                    dp[i, j, r] = (int)(ways % MOD);
                }
            }
        }
        return dp[m - 1, n - 1, 0];
    }
}
