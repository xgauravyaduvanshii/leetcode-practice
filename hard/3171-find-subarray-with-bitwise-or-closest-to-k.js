// LeetCode 3171. Find Subarray With Bitwise OR Closest to K — Hard
// https://leetcode.com/problems/find-subarray-with-bitwise-or-closest-to-k/
// Submission 2202058397 — Accepted, JavaScript
//
// My thinking: the ORs of subarrays
// ending at each position are few — OR
// only gains bits, so at most 32 distinct
// values survive. I keep that small set,
// extend it with each new element, and
// track the closest value to k as I go.

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumDifference = function(nums, k) {
    let ans = Infinity;
    let cur = new Set();
    for (const x of nums) {
        const nxt = new Set([x]);
        for (const v of cur) nxt.add(v | x);
        cur = nxt;
        for (const v of cur) {
            const d = Math.abs(k - v);
            if (d < ans) {
                ans = d;
                if (ans === 0) return 0;
            }
        }
    }
    return ans;
};
