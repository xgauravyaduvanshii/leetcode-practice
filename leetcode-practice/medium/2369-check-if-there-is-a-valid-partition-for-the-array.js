// LeetCode 2369. Check if There is a Valid Partition For The Array — Medium
// https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
// Submission 2204754870 — Accepted, JavaScript
//
// My thinking: same idea as the Python version — backwards DP where
// dp[i] is whether the suffix from i can be partitioned, taking a pair
// of equals, a triple of equals, or three consecutive increasing
// numbers, each only when the remaining suffix is partitionable.
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var validPartition = function(nums) {
    const n = nums.length;
    const dp = new Array(n + 1).fill(false);
    dp[n] = true;
    for (let i = n - 1; i >= 0; i--) {
        if (i + 1 < n && nums[i] === nums[i + 1] && dp[i + 2]) {
            dp[i] = true;
        } else if (i + 2 < n && nums[i] === nums[i + 1] && nums[i + 1] === nums[i + 2] && dp[i + 3]) {
            dp[i] = true;
        } else if (i + 2 < n && nums[i + 1] === nums[i] + 1 && nums[i + 2] === nums[i] + 2 && dp[i + 3]) {
            dp[i] = true;
        }
    }
    return dp[0];
};
