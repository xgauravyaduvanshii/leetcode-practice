// LeetCode 2317. Maximum XOR After Operations — Medium
// https://leetcode.com/problems/maximum-xor-after-operations/
// Submission 2204683872 — Accepted, JavaScript
//
// My thinking: same idea as the Python version — no operation can create
// a bit that no number has, so the maximum XOR is just the OR of all the
// numbers.
/**
 * @param {number[]} nums
 * @return {number}
 */
var maximumXOR = function(nums) {
    let ans = 0;
    for (const x of nums) ans |= x;
    return ans;
};
