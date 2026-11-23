// LeetCode 3082. Find the Sum of the Power of All Subsequences — Hard
// https://leetcode.com/problems/find-the-sum-of-the-power-of-all-subsequences/
// Submission 2201927543 — Accepted, Java
//
// My thinking: instead of counting
// inside every subsequence, I count by
// the inner one. A set T that sums to k
// sits inside exactly 2^(n - |T|)
// subsequences — every other element is
// freely in or out — so the answer is
// the sum of 2^(n - |T|) over all such
// sets T. I count those sets by sum and
// size with a small knapsack DP.

class Solution {
    public int sumOfPower(int[] nums, int k) {
        final int MOD = 1_000_000_007;
        int n = nums.length;
        // dp[s][c]: sets with sum s and c elements.
        long[][] dp = new long[k + 1][n + 1];
        dp[0][0] = 1;
        for (int x : nums) {
            for (int s = k; s >= x; s--) {
                for (int c = n; c >= 1; c--) {
                    dp[s][c] = (dp[s][c] + dp[s - x][c - 1]) % MOD;
                }
            }
        }
        long[] pow2 = new long[n + 1];
        pow2[0] = 1;
        for (int i = 1; i <= n; i++) pow2[i] = pow2[i - 1] * 2 % MOD;
        long ans = 0;
        for (int c = 0; c <= n; c++) {
            ans = (ans + dp[k][c] * pow2[n - c]) % MOD;
        }
        return (int) ans;
    }
}
