// LeetCode 3405. Count the Number of Arrays with K Matching Adjacent Elements — Hard
// https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/
// Submission 2202511952 — Accepted 809/809, TypeScript
//
function countArrays(n: number, m: number, k: number): number {
    // My thinking: pick which k of the n - 1 adjacent slots are
    // the matching ones — C(n - 1, k) ways. Then the first element
    // has m choices, each matching slot is forced to repeat the
    // previous value, and each of the other n - 1 - k slots has
    // m - 1 choices (anything but the previous value). Multiply
    // the three counts, all modulo 1_000_000_007 — BigInt keeps
    // the products exact, since two mod-sized factors exceed
    // the safe integer range.
    const MOD = 1000000007n;
    const fact: bigint[] = new Array(n).fill(1n);
    for (let i = 1; i < n; i++) {
        fact[i] = (fact[i - 1] * BigInt(i)) % MOD;
    }
    const invFact: bigint[] = new Array(n).fill(1n);
    invFact[n - 1] = modPow(fact[n - 1], MOD - 2n, MOD);
    for (let i = n - 1; i > 0; i--) {
        invFact[i - 1] = (invFact[i] * BigInt(i)) % MOD;
    }
    const comb = (a: number, b: number): bigint => {
        if (b < 0 || b > a) return 0n;
        return (((fact[a] * invFact[b]) % MOD) * invFact[a - b]) % MOD;
    };
    const ans = (((comb(n - 1, k) * BigInt(m)) % MOD) * modPow(BigInt(m - 1), BigInt(n - 1 - k), MOD)) % MOD;
    return Number(ans);
}

function modPow(base: bigint, exp: bigint, mod: bigint): bigint {
    let result = 1n;
    let b = base % mod;
    let e = exp;
    while (e > 0n) {
        if (e % 2n === 1n) result = (result * b) % mod;
        b = (b * b) % mod;
        e /= 2n;
    }
    return result;
}
