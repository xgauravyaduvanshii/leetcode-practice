// LeetCode 1955. Count Number of Special Subsequences — Hard
// https://leetcode.com/problems/count-number-of-special-subsequences/
// Submission 2201269441 — Accepted, Rust
//
// My thinking: I count the subsequences that are
// some 0s, then some 1s, then some 2s — each new
// number either doubles the count so far or starts
// a fresh run from the stage before it.

impl Solution {
    pub fn count_special_subsequences(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let (mut dp0, mut dp1, mut dp2) = (0i64, 0i64, 0i64);
        for x in nums {
            match x {
                0 => dp0 = (dp0 * 2 + 1) % MOD,
                1 => dp1 = (dp1 * 2 + dp0) % MOD,
                _ => dp2 = (dp2 * 2 + dp1) % MOD,
            }
        }
        dp2 as i32
    }
}
