// LeetCode 2172. Maximum AND Sum of Array — Hard
// https://leetcode.com/problems/maximum-and-sum-of-array/
// Submission 2201602247 — Accepted, TypeScript
//
// My thinking: each slot holds two numbers,
// so a slot is two switches — I walk through
// the subsets of switches, put the next
// number in every free one, and keep the
// best sum that fills every number.

function maximumANDSum(nums: number[], numSlots: number): number {
    const m = 2 * numSlots;
    const size = 1 << m;
    const dp = new Array<number>(size).fill(-1);
    dp[0] = 0;
    let ans = 0;
    const popcount = (x: number): number => {
        let c = 0;
        while (x) { c += x & 1; x >>= 1; }
        return c;
    };
    for (let mask = 0; mask < size; mask++) {
        if (dp[mask] < 0) continue;
        const used = popcount(mask);
        if (used === nums.length) {
            ans = Math.max(ans, dp[mask]);
            continue;
        }
        for (let b = 0; b < m; b++) {
            if ((mask >> b) & 1) continue;
            const nxt = mask | (1 << b);
            const val = dp[mask] + (nums[used] & (Math.floor(b / 2) + 1));
            if (val > dp[nxt]) dp[nxt] = val;
        }
    }
    return ans;
}
