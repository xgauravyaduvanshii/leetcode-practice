// LeetCode 2348. Number of Zero-Filled Subarrays — Medium
// https://leetcode.com/problems/number-of-zero-filled-subarrays/
// Submission 2204726937 — Accepted, JavaScript
//
// My thinking: same idea as the Python version — grow the current zero
// run and add its length to the answer at each zero; a non-zero resets
// the run.
/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    let ans = 0;
    let run = 0;
    for (const x of nums) {
        if (x === 0) {
            run++;
            ans += run;
        } else {
            run = 0;
        }
    }
    return ans;
};
