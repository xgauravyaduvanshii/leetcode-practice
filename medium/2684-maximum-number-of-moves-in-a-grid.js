// LeetCode 2684. Maximum Number of Moves in a Grid — Medium
// https://leetcode.com/problems/maximum-number-of-moves-in-a-grid/
// Submission 2205193815 — Accepted, JavaScript
//
// My thinking: same idea as the Python version — DP right to
// left, one column at a time; each cell takes one plus the best
// of the three strictly larger neighbours in the next column,
// or 0 when no such neighbour exists.
/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxMoves = function(grid) {
    const m = grid.length, n = grid[0].length;
    let dp = new Array(m).fill(0);
    for (let c = n - 2; c >= 0; c--) {
        const ndp = new Array(m).fill(0);
        for (let r = 0; r < m; r++) {
            let nxt = -1;
            for (const nr of [r - 1, r, r + 1]) {
                if (nr >= 0 && nr < m && grid[nr][c + 1] > grid[r][c]) {
                    nxt = Math.max(nxt, dp[nr]);
                }
            }
            ndp[r] = nxt < 0 ? 0 : nxt + 1;
        }
        dp = ndp;
    }
    return Math.max(...dp);
};
