// LeetCode 3966. Count Good Integers in a Range — Hard
// https://leetcode.com/problems/count-good-integers-in-a-range/
// Submission 2203488719 — Accepted, TypeScript
function goodIntegers(l: number, r: number, k: number): number {
    // My thinking: count the good numbers up to x with
    // a digit DP and answer F(r) - F(l - 1). The DP walks
    // the digits of x tracking whether the prefix is
    // already tight, whether any digit has started, and
    // the previous digit; a new digit is allowed only when
    // it is within k of the previous one. Leading zeros do
    // not start the number, so a one-digit number is
    // always good. There are at most 16 digits, so the
    // memoised states are tiny.
    function countUpTo(x: number): number {
        if (x <= 0) return 0;
        const digits = String(x).split("").map(Number);
        const memo = new Map<string, number>();
        function dfs(pos: number, prev: number, tight: boolean, started: boolean): number {
            if (pos === digits.length) return started ? 1 : 0;
            if (!tight) {
                const hit = memo.get(`${pos},${prev},${started}`);
                if (hit !== undefined) return hit;
            }
            const limit = tight ? digits[pos] : 9;
            let total = 0;
            for (let d = 0; d <= limit; d++) {
                const ntight = tight && d === limit;
                if (!started && d === 0) {
                    total += dfs(pos + 1, -1, ntight, false);
                } else if (!started || Math.abs(d - prev) <= k) {
                    total += dfs(pos + 1, d, ntight, true);
                }
            }
            if (!tight) memo.set(`${pos},${prev},${started}`, total);
            return total;
        }
        return dfs(0, -1, true, false);
    }
    return countUpTo(r) - countUpTo(l - 1);
}
