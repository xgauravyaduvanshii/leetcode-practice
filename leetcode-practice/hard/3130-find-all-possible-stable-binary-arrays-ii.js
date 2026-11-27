// LeetCode 3130. Find All Possible Stable Binary Arrays II — Hard
// https://leetcode.com/problems/find-all-possible-stable-binary-arrays-ii/
// Submission 2202021030 — Accepted, JavaScript
//
// My thinking: I count arrays ending in
// 0 and ending in 1 separately, tracking
// how many of each symbol were used. An
// array ending in 0 extends any array
// ending in 1, plus runs of zeros up to
// the limit — I keep those sums in a
// sliding window, and the same the other
// way round for arrays ending in 1.

var numberOfStableArrays = function(zero, one, limit) {
    const MOD = 1000000007;
    const A = [];
    const B = [];
    const colB = new Array(one + 1).fill(0);
    for (let z = 0; z <= zero; z++) {
        const Arow = new Array(one + 1).fill(0);
        const Brow = new Array(one + 1).fill(0);
        const prevB = z >= 1 ? B[z - 1] : null;
        const dropB = z - limit - 1 >= 0 ? B[z - limit - 1] : null;
        let rowSum = 0;
        for (let o = 0; o <= one; o++) {
            if (prevB) {
                colB[o] += prevB[o];
                if (dropB) colB[o] -= dropB[o];
            }
            if (z > 0) {
                if (o === 0) Arow[o] = z <= limit ? 1 : 0;
                else Arow[o] = colB[o] % MOD;
            }
            if (o >= 1) {
                rowSum += Arow[o - 1];
                if (o - limit - 1 >= 0) rowSum -= Arow[o - limit - 1];
            }
            if (o > 0) {
                if (z === 0) Brow[o] = o <= limit ? 1 : 0;
                else Brow[o] = rowSum % MOD;
            }
        }
        A.push(Arow);
        B.push(Brow);
    }
    return (A[zero][one] + B[zero][one]) % MOD;
};
