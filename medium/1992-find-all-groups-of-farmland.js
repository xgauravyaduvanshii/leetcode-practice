// LeetCode 1992. Find All Groups of Farmland — Medium
// https://leetcode.com/problems/find-all-groups-of-farmland/
// Submission 2204109877 — Accepted, JavaScript

// My thinking:
// Each group of farmland is a solid rectangle of 1s, and different groups
// never touch each other — there is always at least one 0 between them.
// So the top-left corner of a group is easy to spot: a 1 whose cell above
// is a 0 (or the edge of the grid) and whose cell to the left is a 0 (or
// the edge). Every other 1 in the rectangle has a 1 above it or to its
// left, so each group has exactly one such corner.
// From that corner I walk right as long as the cells are 1s to find the
// last column, then walk down as long as the cells are 1s to find the last
// row. That gives the rectangle [r1, c1, r2, c2] for the group, and I
// record it and keep scanning.

/**
 * @param {number[][]} land
 * @return {number[][]}
 */
var findFarmland = function(land) {
    const m = land.length;
    const n = land[0].length;
    const groups = [];
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (land[r][c] === 0) continue;
            // Only a top-left corner starts a new group: a 1 above or
            // to the left means this cell belongs to a group already
            // counted.
            if (r > 0 && land[r - 1][c] === 1) continue;
            if (c > 0 && land[r][c - 1] === 1) continue;
            // Walk right to find the last column of this rectangle.
            let c2 = c;
            while (c2 + 1 < n && land[r][c2 + 1] === 1) c2++;
            // Walk down to find the last row of this rectangle.
            let r2 = r;
            while (r2 + 1 < m && land[r2 + 1][c] === 1) r2++;
            groups.push([r, c, r2, c2]);
        }
    }
    return groups;
};
