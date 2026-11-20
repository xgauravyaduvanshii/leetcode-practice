/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var getLengthOfOptimalCompression = function(s, k) {
    // My thinking: delete up to k letters, then the cost
    // of each run is 1 plus the digits of its length — so
    // remember the last letter and how long its run is.
    const n = s.length;
    function digits(c) {
        if (c === 1) return 0;
        if (c < 10) return 1;
        if (c < 100) return 2;
        return 3;
    }
    const memo = new Map();
    function dp(i, left, last, count) {
        if (left < 0) return Infinity;
        if (i === n) return 0;
        const key = `${i}|${left}|${last}|${count}`;
        const hit = memo.get(key);
        if (hit !== undefined) return hit;
        let best = dp(i + 1, left - 1, last, count);
        if (s[i] === last) {
            best = Math.min(best, dp(i + 1, left, last, count + 1) + digits(count + 1) - digits(count));
        } else {
            best = Math.min(best, dp(i + 1, left, s[i], 1) + 1);
        }
        memo.set(key, best);
        return best;
    }
    return dp(0, k, "", 0);
};
