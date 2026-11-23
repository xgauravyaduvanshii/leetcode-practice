// LeetCode 3229. Minimum Operations to Make Array Equal to Target — Hard
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/
// Submission 2202109144 — Accepted, TypeScript
//
// My thinking: for the differences
// d = target - nums, one operation fixes
// a whole run of the same sign: it costs
// the first |d| in the run plus every
// later increase of |d| inside it. Sign
// changes and zeros start a new run, so I
// just walk the array tracking the
// previous difference.

function minimumOperations(nums: number[], target: number[]): number {
    let total = 0;
    let prev = 0;
    for (let i = 0; i < nums.length; i++) {
        const d = target[i] - nums[i];
        if (d > 0) {
            if (prev > 0) {
                if (d > prev) total += d - prev;
            } else {
                total += d;
            }
        } else if (d < 0) {
            if (prev < 0) {
                if (d < prev) total += prev - d;
            } else {
                total += -d;
            }
        }
        prev = d;
    }
    return total;
};
