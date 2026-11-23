// LeetCode 3145. Find Products of Elements of Big Array — Hard
// https://leetcode.com/problems/find-products-of-elements-of-big-array/
// Submission 2202037091 — Accepted, TypeScript
//
// My thinking: the big array lists the
// powers of two in each integer's binary
// expansion, so the product over a range
// is 2 raised to the sum of the
// exponents. I compute, for any prefix,
// that total exponent sum by walking the
// binary blocks of the prefix — each
// block of size 2^b contributes a known
// count — and answer each query from two
// prefix sums with modular exponentiation.

function findProductsOfElements(queries: number[][]): number[] {
    function prefixExpSum(p: bigint): bigint {
        if (p < 0n) return 0n;
        let rem = p;
        let prefix = 0n;
        let pp = 0n;
        let pe = 0n;
        let expSum = 0n;
        for (let b = 60; b >= 0; b--) {
            const size = 1n << BigInt(b);
            let blockPop: bigint;
            let blockExp: bigint;
            if (b === 0) {
                blockPop = pp;
                blockExp = pe;
            } else {
                blockPop = size * pp + BigInt(b) * (size / 2n);
                blockExp = size * pe + (size / 2n) * BigInt(b) * BigInt(b - 1) / 2n;
            }
            if (rem >= blockPop) {
                rem -= blockPop;
                expSum += blockExp;
                prefix |= size;
                pp += 1n;
                pe += BigInt(b);
            }
        }
        let need = rem + 1n;
        let partial = 0n;
        let bit = 0;
        while (need > 0n) {
            if ((prefix >> BigInt(bit)) & 1n) {
                partial += BigInt(bit);
                need -= 1n;
            }
            bit++;
        }
        return expSum + partial;
    }
    function powMod(exp: bigint, mod: bigint): number {
        let result = 1n;
        let base = 2n % mod;
        let e = exp;
        while (e > 0n) {
            if (e & 1n) result = result * base % mod;
            base = base * base % mod;
            e >>= 1n;
        }
        return Number(result);
    }
    const cache = new Map<bigint, bigint>();
    function cached(p: bigint): bigint {
        let v = cache.get(p);
        if (v === undefined) {
            v = prefixExpSum(p);
            cache.set(p, v);
        }
        return v;
    }
    const ans: number[] = [];
    for (const q of queries) {
        const mod = BigInt(q[2]);
        if (mod === 1n) {
            ans.push(0);
            continue;
        }
        const exp = cached(BigInt(q[1])) - cached(BigInt(q[0]) - 1n);
        ans.push(powMod(exp, mod));
    }
    return ans;
}
