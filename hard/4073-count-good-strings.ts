// LeetCode 4073. Count Good Strings — Hard
// https://leetcode.com/problems/count-good-strings/
// Submission 2203683463 — Accepted, TypeScript
function countGoodStrings(n: number): number {
    // My thinking: let a(n) be the number of good
    // strings of length n. A good string is either
    // a single repeated character of odd length, or
    // a split into two non-empty good parts whose
    // boundary characters differ. Counting the
    // splits by the length of the first part gives
    // the recurrence a(n) = a(n-1) + a(n-2), with
    // a(1) = 2 and a(2) = 2. That is twice the
    // Fibonacci sequence: a(n) = 2 * Fib(n). Since
    // n can be as large as 10^15, compute Fib(n)
    // in O(log n) with the fast-doubling identities
    // F(2k) = F(k) * (2*F(k+1) - F(k)) and
    // F(2k+1) = F(k)^2 + F(k+1)^2, all modulo
    // 10^9 + 7. BigInt is used so the intermediate
    // products stay exact, and the answer is twice
    // F(n).
    const MOD = 1000000007n;
    function fib(k: bigint): [bigint, bigint] {
        if (k === 0n) return [0n, 1n];
        const [a, b] = fib(k >> 1n);
        const c = (a * ((b * 2n - a + MOD) % MOD)) % MOD;
        const d = (a * a + b * b) % MOD;
        if (k & 1n) return [d, (c + d) % MOD];
        return [c, d];
    }
    return Number((2n * fib(BigInt(n))[0]) % MOD);
};
