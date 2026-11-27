// LeetCode 64. Minimum Path Sum — Medium
// https://leetcode.com/problems/minimum-path-sum/
// Submission 2203840235 — Accepted, C#

// My thinking: I fill the grid with the cheapest cost to reach each
// cell, which is the cell's own value plus the cheaper of the costs
// from above and from the left. The first row and column only have one
// way in, so they just accumulate. I reuse one row of costs, updating
// it left to right, and the last cell holds the answer.
public class Solution {
    public int MinPathSum(int[][] grid) {
        int m = grid.Length, n = grid[0].Length;
        int[] dp = new int[n];
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (r == 0 && c == 0) dp[c] = grid[r][c];
                else if (r == 0) dp[c] = dp[c - 1] + grid[r][c];
                else if (c == 0) dp[c] = dp[c] + grid[r][c];
                else dp[c] = Math.Min(dp[c], dp[c - 1]) + grid[r][c];
            }
        }
        return dp[n - 1];
    }
}
