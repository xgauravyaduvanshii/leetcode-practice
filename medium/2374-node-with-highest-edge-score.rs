// LeetCode 2374. Node With Highest Edge Score — Medium
// https://leetcode.com/problems/node-with-highest-edge-score/
// Submission 2204765144 — Accepted, Rust
//
// My thinking: same idea as the Python version — accumulate each edge's
// index into its target node's score, then pick the smallest index with
// the largest score. i64 scores are used because the sum of indices can
// exceed 32 bits.
impl Solution {
    pub fn edge_score(edges: Vec<i32>) -> i32 {
        let n = edges.len();
        let mut score = vec![0i64; n];
        for (i, &v) in edges.iter().enumerate() {
            score[v as usize] += i as i64;
        }
        let mut best = 0usize;
        for i in 1..n {
            if score[i] > score[best] {
                best = i;
            }
        }
        best as i32
    }
}
