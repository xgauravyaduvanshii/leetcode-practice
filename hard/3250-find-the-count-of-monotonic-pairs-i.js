// LeetCode 3250. Find the Count of Monotonic Pairs I — Hard
// https://leetcode.com/problems/find-the-count-of-monotonic-pairs-i/
// Submission 2202139161 — Accepted, JavaScript
//
// My thinking: split each nums[i] into arr1[i]
// + arr2[i] with arr1 non-decreasing and arr2
// non-increasing. I keep a DP over the value of
// arr1[i]; moving to the next number, arr1 must
// grow by at least max(0, nums[i] - nums[i-1])
// to keep arr2 non-increasing, and a prefix sum
// makes each transition O(1).

/**
 * @param {number[]} nums
 * @return {number}
 */
var countOfPairs = function(nums) {
    const MOD = 1000000007;
    let dp = new Array(nums[0] + 1).fill(1);
    for (let i = 1; i < nums.length; i++) {
        const d = nums[i] - nums[i - 1];
        const need = d > 0 ? d : 0;
        const pref = new Array(dp.length + 1).fill(0);
        for (let t = 0; t < dp.length; t++) {
            pref[t + 1] = (pref[t] + dp[t]) % MOD;
        }
        const ndp = new Array(nums[i] + 1).fill(0);
        for (let s = 0; s <= nums[i]; s++) {
            let lim = s - need;
            if (lim >= 0) {
                if (lim >= dp.length) lim = dp.length - 1;
                ndp[s] = pref[lim + 1];
            }
        }
        dp = ndp;
    }
    let ans = 0;
    for (const v of dp) ans = (ans + v) % MOD;
    return ans;
};
