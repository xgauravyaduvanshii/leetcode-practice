// LeetCode 3621. Number of Integers With Popcount-Depth Equal to K I — Hard
// https://leetcode.com/problems/number-of-integers-with-popcount-depth-equal-to-k-i/
// Submission 2202885469 — Accepted, TypeScript
function popcountDepth(n: number, k: number): number {
    // My thinking: the depth of x is one plus the depth of its
    // popcount, so the depth of any number is decided by a
    // popcount of at most 50. I work out the depth of every
    // value up to 50 once, collect the popcounts whose depth is
    // k-1, and count the numbers up to n with one of those
    // popcounts by walking the bits of n. The number 1 itself
    // has popcount 1 but depth 0, so when k is 1 I take it back
    // out of the count.
    function depth(x: number): number {
        let d = 0;
        while (x !== 1) {
            x = x.toString(2).split("1").length - 1;
            d++;
        }
        return d;
    }
    const dep: number[] = [];
    for (let m = 1; m <= 50; m++) dep[m] = depth(m);
    if (k === 0) return 1;
    const P: number[] = [];
    for (let m = 1; m <= 50; m++) if (dep[m] === k - 1) P.push(m);
    if (P.length === 0) return 0;
    function comb(a: number, b: number): number {
        if (b < 0 || b > a) return 0;
        let r = 1;
        for (let i = 0; i < b; i++) r = (r * (a - i)) / (i + 1);
        return Math.round(r);
    }
    function countLeq(N: number, c: number): number {
        const bits = N.toString(2);
        const L = bits.length;
        let count = 0;
        let ones = 0;
        for (let i = 0; i < L; i++) {
            if (bits[i] === "1") {
                const rem = L - i - 1;
                const need = c - ones;
                if (need >= 0 && need <= rem) count += comb(rem, need);
                ones++;
                if (ones > c) return count;
            }
        }
        if (ones === c) count++;
        return count;
    }
    let total = 0;
    for (const c of P) total += countLeq(n, c);
    if (k === 1) total -= 1;
    return total;
}
