// LeetCode 2708. Maximum Strength of a Group — Medium
// https://leetcode.com/problems/maximum-strength-of-a-group/
// Submission 2205198784 — Accepted, Rust
//
// My thinking: same idea as the Python version — all positives,
// negatives in pairs by largest magnitude (drop the smallest
// when the count is odd); if nothing survives, a 0 beats a lone
// negative, and a lone negative is the answer when there is no 0.
impl Solution {
    pub fn max_strength(nums: Vec<i32>) -> i64 {
        let pos: Vec<i64> = nums.iter().cloned().filter(|&x| x > 0).map(|x| x as i64).collect();
        let mut neg: Vec<i64> = nums.iter().cloned().filter(|&x| x < 0).map(|x| x as i64).collect();
        neg.sort_by_key(|&x| -x.abs());
        if neg.len() % 2 == 1 {
            neg.pop();
        }
        if pos.is_empty() && neg.is_empty() {
            if nums.contains(&0) {
                return 0;
            }
            return *nums.iter().max().unwrap() as i64;
        }
        let mut ans: i64 = 1;
        for x in pos.iter().chain(neg.iter()) {
            ans *= *x;
        }
        ans
    }
}
