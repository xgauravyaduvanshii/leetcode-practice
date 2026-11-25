// LeetCode 3655. XOR After Range Multiplication Queries II — Hard
// https://leetcode.com/problems/xor-after-range-multiplication-queries-ii/
// Submission 2202939370 — Accepted, TypeScript
const MOD = 1000000007;

// My thinking: a plain number product is exact only below 2^53,
// but a running value times a modular inverse can reach 10^18,
// so the low bits get rounded away. The low 10 bits of the true
// product are fixed by the low 10 bits of the two factors, so I
// check them — and when they disagree I redo the product exactly
// with BigInt instead of trusting the rounded double.
function mulMod(a: number, b: number): number {
    const prod = a * b;
    if (prod < 9007199254740992) {
        return prod % MOD;
    }
    const low = ((a % 1024) * (b % 1024)) % 1024;
    if (prod % 1024 === low) {
        return prod % MOD;
    }
    return Number((BigInt(a) * BigInt(b)) % 1000000007n);
}

function modPow(base: number, exp: number): number {
    let result = 1;
    let b = base;
    let e = exp;
    while (e > 0) {
        if (e & 1) result = mulMod(result, b);
        b = mulMod(b, b);
        e >>= 1;
    }
    return result;
}

function xorAfterQueries(nums: number[], queries: number[][]): number {
    // My thinking: every query only multiplies, so the order of
    // the queries does not matter — each position ends up as
    // nums[i] times the product of the v's of the queries that
    // touch it. For a big step k there are only a few touched
    // positions, so I update them directly. For a small step k
    // I group the queries by k and use a difference array along
    // each residue class: multiply at the first touched index
    // and by the modular inverse just past the last one, then
    // one sweep carries the running product down each chain.
    const n = nums.length;
    const mult: number[] = new Array(n).fill(1);
    const B = 350;
    const byK = new Map<number, number[][]>();
    for (const [l, r, k, v] of queries) {
        if (!byK.has(k)) byK.set(k, []);
        byK.get(k)!.push([l, r, v]);
    }
    for (const [k, qs] of byK) {
        if (k > B) {
            for (const [l, r, v] of qs) {
                for (let i = l; i <= r; i += k) mult[i] = mulMod(mult[i], v);
            }
        } else {
            const diff: number[] = new Array(n + 1).fill(1);
            for (const [l, r, v] of qs) {
                diff[l] = mulMod(diff[l], v);
                const e = l + Math.floor((r - l) / k) * k;
                if (e + k < n) diff[e + k] = mulMod(diff[e + k], modPow(v, MOD - 2));
            }
            const cur: number[] = new Array(k).fill(1);
            for (let i = 0; i < n; i++) {
                cur[i % k] = mulMod(cur[i % k], diff[i]);
                mult[i] = mulMod(mult[i], cur[i % k]);
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < n; i++) ans ^= mulMod(nums[i], mult[i]);
    return ans;
}
