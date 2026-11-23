// LeetCode 3049. Earliest Second to Mark Indices II — Hard
// https://leetcode.com/problems/earliest-second-to-mark-indices-ii/
// Submission 2201917970 — Accepted, Rust
//
// My thinking: I binary-search the
// earliest second and test a candidate
// directly. An index is reset at its
// first change second — the earliest
// reset leaves the most room to mark it
// afterwards. Resetting an index saves
// its decrements but costs the reset
// second itself, so I keep the resets
// with the biggest savings, dropping the
// smallest whenever too many resets
// crowd one stretch: resets whose first
// change falls in [t, x) each need two
// seconds there (the reset and its mark),
// so at most (x - t) / 2 of them fit.
// Whatever is left must fit in the x
// seconds: one mark per index, the
// remaining decrements, and the resets.

use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct Solution;

impl Solution {
    pub fn earliest_second_to_mark_indices(
        nums: Vec<i32>,
        change_indices: Vec<i32>,
    ) -> i32 {
        let m = change_indices.len() as i32;

        fn can(nums: &[i32], change_indices: &[i32], x: i32) -> bool {
            let n = nums.len();
            // First change second (0-based) of each index, or -1.
            let mut first = vec![-1i64; n];
            for s in 0..x as usize {
                let i = (change_indices[s] - 1) as usize;
                if first[i] < 0 {
                    first[i] = s as i64;
                }
            }
            let total_dec: i64 = nums.iter().map(|&v| v as i64).sum();
            // (first second, saving) for each reset worth doing.
            let mut cands: Vec<(i64, i64)> = (0..n)
                .filter(|&i| nums[i] >= 2 && first[i] >= 0)
                .map(|i| (first[i], nums[i] as i64 - 1))
                .collect();
            cands.sort_by(|a, b| b.0.cmp(&a.0)); // latest first change first
            let mut heap: BinaryHeap<Reverse<i64>> = BinaryHeap::new();
            let mut saving: i64 = 0;
            for (f, sv) in cands {
                heap.push(Reverse(sv));
                saving += sv;
                let cap = (x as i64 - f) / 2;
                while heap.len() as i64 > cap {
                    if let Some(Reverse(min)) = heap.pop() {
                        saving -= min;
                    }
                }
            }
            // Marks + leftover decrements + resets must fit in x.
            n as i64 + total_dec - saving <= x as i64
        }

        if !can(&nums, &change_indices, m) {
            return -1;
        }
        let (mut lo, mut hi) = (1, m);
        while lo < hi {
            let mid = (lo + hi) / 2;
            if can(&nums, &change_indices, mid) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo
    }
}
