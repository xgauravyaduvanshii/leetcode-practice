// LeetCode 2251. Number of Flowers in Full Bloom — Hard
// https://leetcode.com/problems/number-of-flowers-in-full-bloom/
// Submission 2201638807 — Accepted, Rust
//
// My thinking: a flower counts at a moment
// if it has opened but not yet closed — so
// I sort the openings and the closings and
// take opened minus closed for each arrival.

impl Solution {
    pub fn full_bloom_flowers(flowers: Vec<Vec<i32>>, people: Vec<i32>) -> Vec<i32> {
        let mut starts: Vec<i32> = flowers.iter().map(|f| f[0]).collect();
        let mut ends: Vec<i32> = flowers.iter().map(|f| f[1]).collect();
        starts.sort_unstable();
        ends.sort_unstable();
        people
            .iter()
            .map(|&t| {
                let started = starts.partition_point(|&x| x <= t) as i32;
                let ended = ends.partition_point(|&x| x < t) as i32;
                started - ended
            })
            .collect()
    }
}
