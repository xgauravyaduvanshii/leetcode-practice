// LeetCode 2275. Largest Combination With Bitwise AND Greater Than Zero — Medium
// https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
// Submission 2204624339 — Accepted, Rust
//
// My thinking: same idea as the Python version — the AND of a group is
// greater than zero exactly when some bit is set in every number of the
// group, so the answer is the largest count of candidates sharing any
// single bit.
impl Solution {
    pub fn largest_combination(candidates: Vec<i32>) -> i32 {
        let mut ans = 0;
        for b in 0..24 {
            let mut cnt = 0;
            for &x in &candidates {
                if ((x >> b) & 1) == 1 {
                    cnt += 1;
                }
            }
            if cnt > ans {
                ans = cnt;
            }
        }
        ans
    }
}
