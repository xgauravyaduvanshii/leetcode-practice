// LeetCode 1755. Closest Subsequence Sum — Hard
// https://leetcode.com/problems/closest-subsequence-sum/
// Submission 2201145106 — Accepted, TypeScript
//
// My thinking: I split the numbers in half, list
// every subset sum of each half, sort one half, and
// for each sum in the other half I binary-search the
// closest partner to the goal.

function minAbsDifference(nums: number[], goal: number): number {
    function subsetSums(arr: number[]): number[] {
        let sums = [0];
        for (const v of arr) {
            sums = sums.concat(sums.map(s => s + v));
        }
        return sums;
    }
    const n = nums.length;
    const left = subsetSums(nums.slice(0, n >> 1));
    const right = subsetSums(nums.slice(n >> 1)).sort((a, b) => a - b);
    let best = Math.abs(goal);
    for (const s of left) {
        const target = goal - s;
        let lo = 0, hi = right.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (right[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        for (const j of [lo - 1, lo]) {
            if (j >= 0 && j < right.length) {
                best = Math.min(best, Math.abs(s + right[j] - goal));
            }
        }
    }
    return best;
}
