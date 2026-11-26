// LeetCode 4023. Elevator Requests II — Hard
// https://leetcode.com/problems/elevator-requests-ii/
// Submission 2203515044 — Accepted, JavaScript
/**
 * @param {number} n
 * @param {number} start
 * @param {number[]} requests
 * @return {number}
 */
var elevatorRequests = function(n, start, requests) {
    // My thinking: only the relative order of the
    // requested floors matters, so sort them and add
    // the start floor. At any moment the visited
    // floors form one contiguous interval around the
    // start, because the elevator never gains by
    // passing an unvisited floor. Moving to the next
    // unvisited floor on either side costs the
    // distance times the number of requests still
    // unfulfilled — every one of them waits through
    // the whole move, including the destination.
    // dp over intervals [l, r] with the elevator at
    // the left or right end is therefore enough, and
    // only the current interval length needs storing:
    // each step expands the interval by one floor on
    // either side. The answer is the cheaper of the
    // two ways to finish with the whole interval
    // visited.
    const pts = [...new Set([...requests, start])].sort((x, y) => x - y);
    const m = pts.length;
    const s = pts.indexOf(start);
    const INF = Number.MAX_SAFE_INTEGER;
    let dp0 = new Array(m).fill(INF);
    let dp1 = new Array(m).fill(INF);
    dp0[s] = 0;
    dp1[s] = 0;
    for (let length = 1; length < m; length++) {
        const ndp0 = new Array(m).fill(INF);
        const ndp1 = new Array(m).fill(INF);
        const rem = m - length;
        for (let l = 0; l + length <= m; l++) {
            const r = l + length - 1;
            if (l > s || s > r) continue;
            let c = dp0[l];
            if (c < INF) {
                if (l > 0) ndp0[l - 1] = Math.min(ndp0[l - 1], c + (pts[l] - pts[l - 1]) * rem);
                if (r + 1 < m) ndp1[l] = Math.min(ndp1[l], c + (pts[r + 1] - pts[l]) * rem);
            }
            c = dp1[l];
            if (c < INF) {
                if (l > 0) ndp0[l - 1] = Math.min(ndp0[l - 1], c + (pts[r] - pts[l - 1]) * rem);
                if (r + 1 < m) ndp1[l] = Math.min(ndp1[l], c + (pts[r + 1] - pts[r]) * rem);
            }
        }
        dp0 = ndp0;
        dp1 = ndp1;
    }
    return Math.min(dp0[0], dp1[0]);
};
