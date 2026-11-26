// LeetCode 3886. Sum of Sortable Integers — Hard
// https://leetcode.com/problems/sum-of-sortable-integers/
// Submission 2203347582 — Accepted, JavaScript
/**
 * @param {number[]} nums
 * @return {number}
 */
var sortableIntegers = function(nums) {
    // My thinking: sort the whole array once to get S. For a
    // divisor k, each block of length k must rotate into the
    // matching slice of S. A block rotates into sorted order
    // exactly when it has at most one cyclic descent: count
    // descents with a prefix sum, so each block costs O(1),
    // and when there is exactly one descent the wrap from
    // the last element back to the first must not descend
    // either. The block must also hold the same multiset as
    // its slice of S, checked with two modular prefix sums
    // of per-value hashes, again O(1) per block. A block
    // passing both tests rotates into its sorted slice, and
    // every divisor whose blocks all pass adds k to the
    // answer.
    var n = nums.length;
    var S = nums.slice().sort(function(a, b) { return a - b; });
    var desc = new Array(n).fill(0);
    for (var i = 0; i < n - 1; i++) if (nums[i] > nums[i + 1]) desc[i] = 1;
    var prefD = new Array(n + 1).fill(0);
    for (var i = 0; i < n; i++) prefD[i + 1] = prefD[i] + desc[i];
    var MOD1 = 1000000007, MOD2 = 1000000009;
    var r1 = {}, r2 = {};
    for (var i = 0; i < n; i++) {
        var v = nums[i];
        if (!(v in r1)) {
            var h = (v * 2654435761) % 4294967296;
            r1[v] = (h % (MOD1 - 1)) + 1;
            r2[v] = (((h ^ 0x9e3779b9) >>> 0) % (MOD2 - 1)) + 1;
        }
    }
    function prefixHash(arr, r, mod) {
        var p = new Array(n + 1).fill(0);
        for (var i = 0; i < n; i++) p[i + 1] = (p[i] + r[arr[i]]) % mod;
        return p;
    }
    var PN1 = prefixHash(nums, r1, MOD1), PS1 = prefixHash(S, r1, MOD1);
    var PN2 = prefixHash(nums, r2, MOD2), PS2 = prefixHash(S, r2, MOD2);
    var ans = 0;
    for (var k = 1; k <= n; k++) {
        if (n % k !== 0) continue;
        var ok = true;
        for (var b = 0; b < n; b += k) {
            var d = prefD[b + k - 1] - prefD[b];
            if (d > 1) { ok = false; break; }
            if (d === 1 && nums[b + k - 1] > nums[b]) { ok = false; break; }
            if ((PN1[b + k] - PN1[b] + MOD1) % MOD1 !== (PS1[b + k] - PS1[b] + MOD1) % MOD1 ||
                (PN2[b + k] - PN2[b] + MOD2) % MOD2 !== (PS2[b + k] - PS2[b] + MOD2) % MOD2) {
                ok = false; break;
            }
        }
        if (ok) ans += k;
    }
    return ans;
};
