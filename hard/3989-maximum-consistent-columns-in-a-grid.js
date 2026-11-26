// LeetCode 3989. Maximum Consistent Columns in a Grid — Hard
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/
// Submission 2203499733 — Accepted, JavaScript
/**
 * @param {number[][]} grid
 * @param {number} limit
 * @return {number}
 */
var maxConsistentColumns = function(grid, limit) {
    // My thinking: the kept columns keep their order,
    // so this is a longest-subsequence problem over
    // columns: dp[j] is the longest consistent run
    // ending at column j, and i can precede j exactly
    // when every row differs by at most limit between
    // the two columns. Checking a pair costs O(m) with
    // an early break on the first row that violates
    // the limit, so the whole DP is O(n^2 * m) with
    // n, m <= 250. A single column is always
    // consistent, so dp starts at 1.
    var m = grid.length;
    var n = grid[0].length;
    var dp = new Array(n).fill(1);
    for (var j = 0; j < n; j++) {
        var best = 1;
        for (var i = 0; i < j; i++) {
            var ok = true;
            for (var r = 0; r < m; r++) {
                if (Math.abs(grid[r][j] - grid[r][i]) > limit) {
                    ok = false;
                    break;
                }
            }
            if (ok && dp[i] + 1 > best) best = dp[i] + 1;
        }
        dp[j] = best;
    }
    return Math.max.apply(null, dp);
};
