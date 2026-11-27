// LeetCode 2350. Shortest Impossible Sequence of Rolls — Hard
// https://leetcode.com/problems/shortest-impossible-sequence-of-rolls/
// Submission 2201694971 — Accepted, Rust
//
// My thinking: a sequence only survives
// while every face keeps showing up — I
// count how many full rounds of all faces
// the rolls hold, and the shortest one
// they lack is one longer than that.

use std::collections::HashSet;

impl Solution {
    pub fn shortest_sequence(rolls: Vec<i32>, k: i32) -> i32 {
        let mut rounds = 0;
        let mut seen: HashSet<i32> = HashSet::new();
        for r in rolls {
            seen.insert(r);
            if seen.len() as i32 == k {
                rounds += 1;
                seen.clear();
            }
        }
        rounds + 1
    }
}
