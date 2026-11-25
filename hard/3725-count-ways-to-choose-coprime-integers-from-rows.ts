// LeetCode 3725. Count Ways to Choose Coprime Integers from Rows — Hard
// https://leetcode.com/problems/count-ways-to-choose-coprime-integers-from-rows/
// Submission 2203132638 — Accepted, TypeScript
function countCoprime(mat: number[][]): number {
    // My thinking: the gcd of the chosen numbers is 1 exactly
    // when no prime divides all of them, so Mobius inversion
    // over the divisor d does the counting: for each d, count
    // the choices whose numbers are all multiples of d (a
    // product over the rows of the per-row multiple counts),
    // then add them up weighted by mu(d). Values are at most
    // 150, so a linear sieve gives mu up to 150 and each row's
    // multiple counts come from one frequency pass. Every
    // product here stays far below 2^53, so plain doubles are
    // exact.
    const MOD = 1000000007;
    const MAXV = 150;
    const mu: number[] = new Array(MAXV + 1).fill(0);
    mu[1] = 1;
    const primes: number[] = [];
    const isComp: boolean[] = new Array(MAXV + 1).fill(false);
    for (let i = 2; i <= MAXV; i++) {
        if (!isComp[i]) {
            primes.push(i);
            mu[i] = -1;
        }
        for (const p of primes) {
            if (i * p > MAXV) break;
            isComp[i * p] = true;
            if (i % p === 0) {
                mu[i * p] = 0;
                break;
            }
            mu[i * p] = -mu[i];
        }
    }
    // Per row, how many entries are multiples of each d.
    const rowMults: number[][] = [];
    for (const row of mat) {
        const freq: number[] = new Array(MAXV + 1).fill(0);
        for (const x of row) freq[x]++;
        const mult: number[] = new Array(MAXV + 1).fill(0);
        for (let d = 1; d <= MAXV; d++) {
            let s = 0;
            for (let m = d; m <= MAXV; m += d) s += freq[m];
            mult[d] = s;
        }
        rowMults.push(mult);
    }
    let ans = 0;
    for (let d = 1; d <= MAXV; d++) {
        if (mu[d] === 0) continue;
        let prod = 1;
        for (const mult of rowMults) {
            prod = (prod * mult[d]) % MOD;
            if (prod === 0) break;
        }
        ans = (ans + mu[d] * prod) % MOD;
    }
    return (ans + MOD) % MOD;
}
