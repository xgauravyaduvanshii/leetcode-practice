// LeetCode 63. Unique Paths II — Medium
// https://leetcode.com/problems/unique-paths-ii/
// Submission 2203839004 — Accepted, TypeScript

// My thinking: I count the ways to reach each cell with dynamic
// programming: a cell's count is the sum of the counts from above and
// from the left, because every path arrives through one of those two.
// Obstacles get zero, the start cell gets one unless it is blocked,
// and I reuse a single row of counts since each row only needs the one
// above it.
function uniquePathsWithObstacles(obstacleGrid: number[][]): number {
    const m = obstacleGrid.length;
    const n = obstacleGrid[0].length;
    const dp = new Array(n).fill(0);
    dp[0] = obstacleGrid[0][0] === 0 ? 1 : 0;
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (obstacleGrid[r][c] === 1) {
                dp[c] = 0;
            } else if (c > 0) {
                dp[c] += dp[c - 1];
            }
        }
    }
    return dp[n - 1];
}
