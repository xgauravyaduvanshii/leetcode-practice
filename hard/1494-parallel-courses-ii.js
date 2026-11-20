/**
 * @param {number} n
 * @param {number[][]} relations
 * @param {number} k
 * @return {number}
 */
var minNumberOfSemesters = function(n, relations, k) {
    // My thinking: a semester is a set of courses whose
    // prerequisites are already done — so track which
    // courses are done as a bitmask and try every
    // affordable batch of the newly available ones.
    const prereq = new Array(n).fill(0);
    for (const [prev, nxt] of relations) prereq[nxt - 1] |= 1 << (prev - 1);
    const INF = Infinity;
    const dp = new Array(1 << n).fill(INF);
    dp[0] = 0;
    function popcount(x) { let c = 0; while (x) { c += x & 1; x >>= 1; } return c; }
    for (let mask = 0; mask < (1 << n); mask++) {
        let avail = 0;
        for (let i = 0; i < n; i++) {
            if (!(mask & (1 << i)) && (prereq[i] & ~mask) === 0) avail |= 1 << i;
        }
        if (avail === 0) continue;
        if (popcount(avail) <= k) {
            dp[mask | avail] = Math.min(dp[mask | avail], dp[mask] + 1);
            continue;
        }
        let sub = avail;
        while (sub) {
            if (popcount(sub) <= k) dp[mask | sub] = Math.min(dp[mask | sub], dp[mask] + 1);
            sub = (sub - 1) & avail;
        }
    }
    return dp[(1 << n) - 1];
};
