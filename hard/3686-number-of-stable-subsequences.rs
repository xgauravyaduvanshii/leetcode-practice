// LeetCode 3686. Number of Stable Subsequences — Hard
// https://leetcode.com/problems/number-of-stable-subsequences/
// Submission 2203040859 — Accepted, Rust
//
const MOD: i64 = 1_000_000_007;

impl Solution {
    pub fn count_stable_subsequences(nums: Vec<i32>) -> i32 {
        // My thinking: a subsequence is stable unless it ever
        // holds three in a row of the same parity, so all I need
        // to remember about a subsequence's tail is its parity
        // and whether its current run is 1 or 2 long. For each
        // new number I either start a fresh subsequence with it,
        // extend any subsequence ending in the opposite parity
        // (its run goes back to 1), or extend one ending in the
        // same parity with run 1 (its run becomes 2) — a run-2
        // tail can never grow, so three in a row never forms.
        let mut dp = [[0i64; 3]; 2];
        for x in nums {
            let q = (x & 1) as usize;
            let add1 = (1 + dp[1 - q][1] + dp[1 - q][2]) % MOD;
            let add2 = dp[q][1];
            dp[q][1] = (dp[q][1] + add1) % MOD;
            dp[q][2] = (dp[q][2] + add2) % MOD;
        }
        ((dp[0][1] + dp[0][2] + dp[1][1] + dp[1][2]) % MOD) as i32
    }
}
