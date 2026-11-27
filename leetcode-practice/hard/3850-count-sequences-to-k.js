// LeetCode 3850. Count Sequences to K — Hard
// https://leetcode.com/problems/count-sequences-to-k/
// Submission 2203294643 — Accepted, JavaScript
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countSequences = function(nums, k) {
    // My thinking: multiplying or dividing by nums[i] only
    // moves the exponents of 2, 3 and 5 in the value, since
    // every nums[i] is at most 6, so the final value is k
    // exactly when the three exponent sums match the
    // exponents of k — and if k has any other prime factor
    // the answer is 0 at once. Each element contributes
    // its exponent vector, its negation, or nothing, so I
    // split the array in half, enumerate all 3^10 choices
    // per half into maps from exponent triple to count, and
    // pair a triple from the first half with the matching
    // complement from the second.
    var primes = [2, 3, 5];
    var target = [];
    var kk = k;
    primes.forEach(function(p) {
        var e = 0;
        while (kk % p === 0) { kk /= p; e++; }
        target.push(e);
    });
    if (kk !== 1) return 0;
    var exps = nums.map(function(v) {
        return primes.map(function(p) {
            var e = 0;
            while (v % p === 0) { v /= p; e++; }
            return e;
        });
    });
    function half(es) {
        var d = new Map();
        function rec(i, a2, a3, a5) {
            if (i === es.length) {
                var key = a2 + ',' + a3 + ',' + a5;
                d.set(key, (d.get(key) || 0) + 1);
                return;
            }
            var e = es[i];
            rec(i + 1, a2, a3, a5);
            rec(i + 1, a2 + e[0], a3 + e[1], a5 + e[2]);
            rec(i + 1, a2 - e[0], a3 - e[1], a5 - e[2]);
        }
        rec(0, 0, 0, 0);
        return d;
    }
    var mid = Math.floor(exps.length / 2);
    var first = half(exps.slice(0, mid));
    var second = half(exps.slice(mid));
    var ans = 0;
    first.forEach(function(c, key) {
        var parts = key.split(',').map(Number);
        var need = (target[0] - parts[0]) + ',' + (target[1] - parts[1]) + ',' + (target[2] - parts[2]);
        ans += c * (second.get(need) || 0);
    });
    return ans;
};
