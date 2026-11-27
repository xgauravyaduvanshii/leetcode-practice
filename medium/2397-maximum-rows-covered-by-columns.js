// LeetCode 2397. Maximum Rows Covered by Columns — Medium
// https://leetcode.com/problems/maximum-rows-covered-by-columns/
// Submission 2204781263 — Accepted, JavaScript
//
// My thinking: same idea as the Python version — try every subset of
// exactly numSelect columns (rows as bitmasks); a row is covered when
// row & ~sel is 0, and the best subset wins.
/**
 * @param {number[][]} matrix
 * @param {number} numSelect
 * @return {number}
 */
var maximumRows = function(matrix, numSelect) {
    const n = matrix[0].length;
    const rows = [];
    for (const row of matrix) {
        let mask = 0;
        for (let j = 0; j < row.length; j++) {
            if (row[j]) mask |= 1 << j;
        }
        rows.push(mask);
    }
    let best = 0;
    for (let sel = 0; sel < (1 << n); sel++) {
        let bits = 0;
        for (let j = 0; j < n; j++) if (sel & (1 << j)) bits++;
        if (bits !== numSelect) continue;
        let covered = 0;
        for (const r of rows) {
            if ((r & ~sel) === 0) covered++;
        }
        if (covered > best) best = covered;
    }
    return best;
};
