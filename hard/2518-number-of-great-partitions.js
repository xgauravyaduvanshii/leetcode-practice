// LeetCode 2518. Number of Great Partitions — Hard
// https://leetcode.com/problems/number-of-great-partitions/
// Submission 2201795923 — Accepted, JavaScript
//
// My thinking: a partition fails when
// either side falls short of k, so I
// count the subsets that fall short —
// each one spoils two orderings — and
// take them away from every possible
// split of the array.

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var countPartitions = function(nums, k) {
  const MOD = 1000000007;
  if (nums.reduce((a, b) => a + b, 0) < 2 * k) return 0;
  const dp = new Array(k).fill(0);
  dp[0] = 1;
  for (const x of nums) {
    for (let s = k - 1; s >= 0; s--) {
      if (s + x < k) dp[s + x] = (dp[s + x] + dp[s]) % MOD;
    }
  }
  const bad = dp.reduce((a, b) => (a + b) % MOD, 0);
  let pow2 = 1;
  for (let i = 0; i < nums.length; i++) pow2 = (pow2 * 2) % MOD;
  return (((pow2 - 2 * bad) % MOD) + MOD) % MOD;
};
