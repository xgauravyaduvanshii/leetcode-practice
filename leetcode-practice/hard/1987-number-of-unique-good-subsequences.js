// LeetCode 1987. Number of Unique Good Subsequences — Hard
// https://leetcode.com/problems/number-of-unique-good-subsequences/
// Submission 2201292941 — Accepted, JavaScript
//
// My thinking: a 1 extends every good run so far
// plus itself, while a 0 only extends the runs
// ending in 1 — and the lone 0 counts once at the
// end, since a leading zero is never allowed.

function numberOfUniqueGoodSubsequences(binary) {
    const MOD = 1_000_000_007;
    let f0 = 0, f1 = 0, hasZero = false;
    for (const ch of binary) {
        if (ch === '1') {
            f1 = (f1 + f0 + 1) % MOD;
        } else {
            hasZero = true;
            f0 = (f0 + f1) % MOD;
        }
    }
    return (f0 + f1 + (hasZero ? 1 : 0)) % MOD;
}
