// LeetCode 3791. Number of Balanced Integers in a Range — Hard
// https://leetcode.com/problems/number-of-balanced-integers-in-a-range/
// Submission 2203181634 — Accepted, TypeScript
function countBalanced(low: number, high: number): number {
    // My thinking: a number is balanced when the digits in odd
    // positions (from the left) sum to the same as the digits
    // in even positions, and it has at least two digits. Count
    // balanced numbers up to x with a digit DP over the decimal
    // string of x, tracking the running difference (odd-position
    // sum minus even-position sum) and whether the prefix is
    // still tight to x; a number is counted when the difference
    // ends at zero. Leading zeroes only shift the positions,
    // which flips the sign of the difference but keeps zero at
    // zero, and the number 0 itself is counted once on both
    // sides, so the answer is count(high) - count(low - 1).
    // Single-digit numbers have a nonzero difference, so the
    // two-digit minimum takes care of itself.
    const countUpto = (x: number): number => {
        if (x < 0) return 0;
        const s = String(x);
        const memo = new Map<string, number>();
        const dfs = (pos: number, diff: number, tight: boolean): number => {
            if (pos === s.length) return diff === 0 ? 1 : 0;
            const key = `${pos},${diff},${tight ? 1 : 0}`;
            const hit = memo.get(key);
            if (hit !== undefined) return hit;
            const limit = tight ? Number(s[pos]) : 9;
            let total = 0;
            for (let d = 0; d <= limit; d++) {
                const ndiff = pos % 2 === 0 ? diff + d : diff - d;
                total += dfs(pos + 1, ndiff, tight && d === limit);
            }
            memo.set(key, total);
            return total;
        };
        return dfs(0, 0, true);
    };
    return countUpto(high) - countUpto(low - 1);
}
