// LeetCode 1866. Number of Ways to Rearrange Sticks With K Sticks Visible — Hard
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/
// Submission 2201210281 — Accepted, Rust
//
// My thinking: the tallest stick splits the row —
// put it at the right end and the sticks to its
// left form a smaller visible arrangement, or
// place it anywhere else and it hides behind a
// taller stick. That gives the Stirling numbers
// of the first kind: dp[i][j] = dp[i-1][j-1] +
// (i-1) * dp[i-1][j], all modulo 1e9+7.

impl Solution {
    pub fn rearrange_sticks(n: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let k = k as usize;
        let mut dp = vec![vec![0i64; k + 1]; n + 1];
        dp[0][0] = 1;
        for i in 1..=n {
            for j in 1..=k.min(i) {
                dp[i][j] = (dp[i - 1][j - 1] + (i as i64 - 1) * dp[i - 1][j]) % MOD;
            }
        }
        dp[n][k] as i32
    }
}
