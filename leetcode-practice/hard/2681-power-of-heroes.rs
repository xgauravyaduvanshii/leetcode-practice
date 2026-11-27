// LeetCode 2681. Power of Heroes — Hard
// https://leetcode.com/problems/power-of-heroes/
// Submission 2201869237 — Accepted, Rust
//
// My thinking: once the strengths are
// sorted, every group is ruled by its
// biggest hero, and the smaller ones in
// between can join or stay home freely
// — so I sweep once, carrying forward
// the sum of every smaller hero times
// the ways it could have been chosen.

impl Solution {
    pub fn sum_of_power(nums: Vec<i32>) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let mut nums: Vec<i64> = nums.into_iter().map(|x| x as i64).collect();
        nums.sort_unstable();
        let mut prev: i64 = 0;
        let mut ans: i64 = 0;
        for x in nums {
            ans = (ans + x * x % MOD * ((x + prev) % MOD)) % MOD;
            prev = (2 * prev + x) % MOD;
        }
        ans as i32
    }
}
