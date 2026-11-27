// LeetCode 2304. Minimum Path Cost in a Grid — Medium
// https://leetcode.com/problems/minimum-path-cost-in-a-grid/
// Submission 2204662677 — Accepted, TypeScript
//
// My thinking: same idea as the Python version — one rolling DP row; the
// cost of entering a cell is its own value plus the cheapest arrival,
// min over k of dp[k] + moveCost[value above in column k][j].
function minPathCost(grid: number[][], moveCost: number[][]): number {
    const m = grid.length;
    const n = grid[0].length;
    let dp = grid[0].slice();
    for (let i = 1; i < m; i++) {
        const ndp: number[] = new Array(n).fill(0);
        for (let j = 0; j < n; j++) {
            let best = Infinity;
            for (let k = 0; k < n; k++) {
                best = Math.min(best, dp[k] + moveCost[grid[i - 1][k]][j]);
            }
            ndp[j] = grid[i][j] + best;
        }
        dp = ndp;
    }
    return Math.min(...dp);
};
