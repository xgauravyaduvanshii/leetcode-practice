// LeetCode 3449. Maximize the Minimum Game Score — Hard
// https://leetcode.com/problems/maximize-the-minimum-game-score/
// Submission 2202545689 — Accepted 692/692, JavaScript
/**
 * @param {number[]} points
 * @param {number} m
 * @return {number}
 */
var maximizeMinimumGameScore = function(points, m) {
    // My thinking: binary-search the answer X, and check it by
    // walking left to right. Each index i needs ceil(X / points[i])
    // visits; arriving there gives one, and any shortfall is
    // topped up by bouncing to the next index and back, which
    // costs 2 moves and also gives the neighbour a visit (the
    // last index bounces left instead). Stop as soon as every
    // index has enough visits, and fail as soon as moves exceed m.
    const n = points.length;
    const can = (x) => {
        const need = points.map(p => Math.floor((x + p - 1) / p));
        const visits = new Array(n).fill(0);
        let remaining = need.filter(v => v > 0).length;
        let moves = 0;
        const add = (j, delta) => {
            const before = visits[j];
            visits[j] += delta;
            if (before < need[j] && need[j] <= visits[j]) remaining--;
        };
        for (let i = 0; i < n; i++) {
            if (remaining === 0) break;
            add(i, 1);
            moves += 1;
            if (moves > m) return false;
            if (remaining === 0) break;
            if (visits[i] < need[i]) {
                const extra = need[i] - visits[i];
                if (i < n - 1) {
                    add(i, extra);
                    add(i + 1, extra);
                } else {
                    add(i, extra);
                    add(i - 1, extra);
                }
                moves += 2 * extra;
                if (moves > m) return false;
            }
            if (remaining === 0) break;
        }
        return moves <= m;
    };
    let lo = 0, hi = m * Math.max(...points);
    while (lo < hi) {
        const mid = Math.floor((lo + hi + 1) / 2);
        if (can(mid)) lo = mid;
        else hi = mid - 1;
    }
    return lo;
};
