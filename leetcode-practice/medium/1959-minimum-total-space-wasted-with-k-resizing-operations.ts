// LeetCode 1959. Minimum Total Space Wasted With K Resizing Operations — Medium
// https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/
// Submission 2204260003 — Accepted, TypeScript

// My thinking: k resizing operations cut the array into k + 1
// segments, and each segment is resized once to its own maximum,
// so a segment's waste is its maximum times its length minus the
// sum of its numbers. The best total is a dynamic program: dp[i][j]
// is the least waste for the first i numbers cut into j segments,
// and I try every possible start for the last segment, adding its
// waste to the best cost of everything before it. A prefix sum
// makes each segment's waste a constant-time lookup.
function minSpaceWastedKResizing(nums: number[], k: number): number {
    const n = nums.length;
    const prefix: number[] = [0];
    for (const x of nums) prefix.push(prefix[prefix.length - 1] + x);

    const waste = (lo: number, hi: number): number => {
        let mx = 0;
        for (let i = lo; i <= hi; i++) mx = Math.max(mx, nums[i]);
        return mx * (hi - lo + 1) - (prefix[hi + 1] - prefix[lo]);
    };

    const segments = Math.min(k + 1, n);
    const dp: number[][] = Array.from({ length: n + 1 }, () =>
        new Array(segments + 1).fill(Infinity),
    );
    dp[0][0] = 0;
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= Math.min(i, segments); j++) {
            for (let p = j - 1; p < i; p++) {
                dp[i][j] = Math.min(dp[i][j], dp[p][j - 1] + waste(p, i - 1));
            }
        }
    }
    return Math.min(...dp[n].slice(1));
}
