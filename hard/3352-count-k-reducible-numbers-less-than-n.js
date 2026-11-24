// LeetCode 3352. Count K-Reducible Numbers Less Than N — Hard
// https://leetcode.com/problems/count-k-reducible-numbers-less-than-n/
// Submission 2202416384 — Accepted, JavaScript
//
// My thinking: one operation replaces x by its popcount, so after the first
// operation the value is at most len(s), and the remaining steps depend only
// on the popcount. I precompute steps[c], the operations needed to reduce c
// to 1, then count binary strings below s by popcount with a digit DP: at
// each '1' in s I count the completions with a smaller bit here, using
// binomial coefficients. A number is k-reducible exactly when
// steps[popcount] <= k - 1.

/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var countKReducible = function(s, k) {
    const MOD = 1000000007;
    const L = s.length;
    const steps = new Array(L + 1).fill(0);
    for (let c = 2; c <= L; c++) {
        let pc = 0, v = c;
        while (v) { pc += v & 1; v >>= 1; }
        steps[c] = 1 + steps[pc];
    }
    const C = Array.from({length: L + 1}, () => new Array(L + 1).fill(0));
    for (let i = 0; i <= L; i++) {
        C[i][0] = C[i][i] = 1;
        for (let j = 1; j < i; j++) C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
    }
    let ans = 0, ones = 0;
    for (let i = 0; i < L; i++) {
        if (s[i] === '1') {
            const rem = L - 1 - i;
            for (let c = 0; c <= rem; c++) {
                const pc = ones + c;
                if (pc >= 1 && steps[pc] <= k - 1) ans = (ans + C[rem][c]) % MOD;
            }
            ones++;
        }
    }
    return ans;
};
