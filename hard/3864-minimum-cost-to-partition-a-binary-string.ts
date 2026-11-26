// LeetCode 3864. Minimum Cost to Partition a Binary String — Hard
// https://leetcode.com/problems/minimum-cost-to-partition-a-binary-string/
// Submission 2203324289 — Accepted, TypeScript
function minCost(s: string, encCost: number, flatCost: number): number {
    // My thinking: a split only ever cuts an even-length
    // segment into two equal halves, so every segment
    // that can appear is [l, l + L) with L in n, n/2,
    // n/4, ... — only O(n) such segments exist, arranged
    // as a binary tree. dp(l, L) is the cheapest cost of
    // partitioning that segment: either keep it whole,
    // costing flatCost when it holds no '1' and
    // L * X * encCost for X ones otherwise, or, when L
    // is even, split it and add the two halves. Prefix
    // sums give each segment's one-count in O(1), and
    // memoisation makes the whole tree O(n). Costs stay
    // below 10^15, safely inside a JS number.
    const n = s.length;
    const pref: number[] = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) pref[i + 1] = pref[i] + (s[i] === "1" ? 1 : 0);
    const memo = new Map<string, number>();
    function dp(l: number, len: number): number {
        const key = l + "," + len;
        const hit = memo.get(key);
        if (hit !== undefined) return hit;
        const ones = pref[l + len] - pref[l];
        const leaf = ones === 0 ? flatCost : len * ones * encCost;
        let best = leaf;
        if (len % 2 === 0) {
            const half = len / 2;
            best = Math.min(best, dp(l, half) + dp(l + half, half));
        }
        memo.set(key, best);
        return best;
    }
    return dp(0, n);
}
