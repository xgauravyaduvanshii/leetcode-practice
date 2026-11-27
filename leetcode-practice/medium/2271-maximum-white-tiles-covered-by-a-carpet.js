// LeetCode 2271. Maximum White Tiles Covered by a Carpet — Medium
// https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/
// Submission 2204614058 — Accepted, JavaScript
//
// My thinking: same idea as the Python version — sort the tiles, build
// prefix sums of their lengths, and for each tile as the carpet's left
// edge find the last tile starting inside the carpet (binary search,
// written out by hand since JavaScript has no bisect) and add the whole
// tiles plus the partial overlap of that last tile.
/**
 * @param {number[][]} tiles
 * @param {number} carpetLen
 * @return {number}
 */
var maximumWhiteTiles = function(tiles, carpetLen) {
    tiles.sort((a, b) => a[0] - b[0]);
    const starts = tiles.map(t => t[0]);
    const pref = [0];
    for (const [l, r] of tiles) pref.push(pref[pref.length - 1] + r - l + 1);
    let ans = 0;
    for (let i = 0; i < tiles.length; i++) {
        const end = tiles[i][0] + carpetLen - 1;
        let lo = 0, hi = starts.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (starts[mid] <= end) lo = mid + 1;
            else hi = mid;
        }
        const k = lo - 1;
        let covered = pref[k] - pref[i];
        covered += Math.min(tiles[k][1], end) - tiles[k][0] + 1;
        ans = Math.max(ans, covered);
    }
    return ans;
};
