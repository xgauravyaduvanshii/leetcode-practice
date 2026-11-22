// LeetCode 1830. Minimum Number of Operations to Make String Sorted — Hard
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted/
// Submission 2201191418 — Accepted, TypeScript
//
// My thinking: the answer is how many distinct
// arrangements of the same letters come before
// this string — at each position I try every
// smaller letter still unused and count the
// arrangements of what is left. Factorials are
// multiplied with BigInt so the modular products
// stay exact.

const MOD = 1000000007n;

function modPow(base: bigint, exp: bigint): bigint {
    let res = 1n;
    while (exp > 0n) {
        if (exp & 1n) res = (res * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1n;
    }
    return res;
}

function makeStringSorted(s: string): number {
    const n = s.length;
    const fact: bigint[] = [1n];
    for (let i = 1; i <= n; i++) fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    const invFact: bigint[] = new Array(n + 1);
    invFact[n] = modPow(fact[n], MOD - 2n);
    for (let i = n; i > 0; i--) invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    const cnt = new Array(26).fill(0);
    for (const ch of s) cnt[ch.charCodeAt(0) - 97]++;
    let ans = 0n;
    for (let i = 0; i < n; i++) {
        const cur = s.charCodeAt(i) - 97;
        for (let c = 0; c < cur; c++) {
            if (cnt[c] === 0) continue;
            let denom = 1n;
            for (let k = 0; k < 26; k++) {
                denom = (denom * (k === c ? invFact[cnt[k] - 1] : invFact[cnt[k]])) % MOD;
            }
            ans = (ans + fact[n - 1 - i] * denom) % MOD;
        }
        cnt[cur]--;
    }
    return Number(ans);
}
