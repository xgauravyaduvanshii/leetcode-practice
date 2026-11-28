// LeetCode 2711. Difference of Number of Distinct Values on Diagonals — Medium
// https://leetcode.com/problems/difference-of-number-of-distinct-values-on-diagonals/
// Submission 2205205120 — Accepted, TypeScript
//
// My thinking: same idea as the Python version — walk each
// cell's diagonal up-left and down-right into two sets and
// take the absolute difference of their sizes.
function differenceOfDistinctValues(grid: number[][]): number[][] {
    const m = grid.length, n = grid[0].length;
    const ans: number[][] = Array.from({ length: m }, () => new Array(n).fill(0));
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            const up = new Set<number>();
            for (let i = r - 1, j = c - 1; i >= 0 && j >= 0; i--, j--) up.add(grid[i][j]);
            const down = new Set<number>();
            for (let i = r + 1, j = c + 1; i < m && j < n; i++, j++) down.add(grid[i][j]);
            ans[r][c] = Math.abs(up.size - down.size);
        }
    }
    return ans;
}
