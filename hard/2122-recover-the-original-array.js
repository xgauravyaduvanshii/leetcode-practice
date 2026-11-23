// LeetCode 2122. Recover the Original Array — Hard
// https://leetcode.com/problems/recover-the-original-array/
// Submission 2201580090 — Accepted, JavaScript
//
// My thinking: the smallest number left must
// be some original minus k — a plus-k twin
// would leave its smaller minus-k partner
// behind — so I take the smallest, pair it
// with the number 2k above it, and keep going.

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var recoverArray = function(nums, k) {
    const counts = new Map();
    for (const x of nums) counts.set(x, (counts.get(x) ?? 0) + 1);
    const ans = [];
    for (const x of [...counts.keys()].sort((a, b) => a - b)) {
        while ((counts.get(x) ?? 0) > 0) {
            counts.set(x, counts.get(x) - 1);
            counts.set(x + 2 * k, (counts.get(x + 2 * k) ?? 0) - 1);
            ans.push(x + k);
        }
    }
    return ans;
};
