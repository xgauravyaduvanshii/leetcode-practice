// LeetCode 2321. Maximum Score Of Spliced Array — Hard
// https://leetcode.com/problems/maximum-score-of-spliced-array/
// Submission 2201676485 — Accepted, TypeScript
//
// My thinking: swapping one stretch adds
// the other array's gain and takes away
// mine, so I run Kadane on the difference
// both ways and keep whichever side ends
// up richer.

function maximumsSplicedArray(nums1: number[], nums2: number[]): number {
    const maxGain = (diff: number[]): number => {
        let best = 0;
        let cur = 0;
        for (const d of diff) {
            cur = Math.max(0, cur + d);
            best = Math.max(best, cur);
        }
        return best;
    };
    const sum1 = nums1.reduce((a, b) => a + b, 0);
    const sum2 = nums2.reduce((a, b) => a + b, 0);
    const diff1 = nums1.map((a, i) => nums2[i] - a);
    const diff2 = nums1.map((a, i) => a - nums2[i]);
    return Math.max(sum1 + maxGain(diff1), sum2 + maxGain(diff2));
}
