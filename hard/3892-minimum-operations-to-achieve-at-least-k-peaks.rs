// LeetCode 3892. Minimum Operations to Achieve At Least K Peaks — Hard
// https://leetcode.com/problems/minimum-operations-to-achieve-at-least-k-peaks/
// Submission 2203357625 — Accepted, Rust
//
// My thinking: raising a peak never hurts another peak,
// because peaks are never adjacent and a peak's raised
// value is not a neighbour of any other peak, and raising
// a non-peak only makes peaks harder. So each index i has
// an independent price: how much it must rise to beat
// both of its original neighbours, or 0 if it already
// does. The task becomes picking k non-adjacent indices
// of minimum total price on a cycle. That is a small DP
// over a path — dp0[t] the cheapest price with t peaks
// and the last index not taken, dp1[t] with it taken —
// run twice to break the cycle: once with index 0
// forbidden, once with index 0 taken (paying its price
// and forbidding its two neighbours). More than n / 2
// peaks is impossible on a cycle, and k = 0 costs
// nothing.
use std::cmp::min;

const INF: i64 = i64::MAX / 4;

fn path_dp(cs: &[i64], t: usize) -> i64 {
    let mut dp0 = vec![INF; t + 1];
    let mut dp1 = vec![INF; t + 1];
    dp0[0] = 0;
    for &c in cs {
        let mut ndp0 = vec![INF; t + 1];
        let mut ndp1 = vec![INF; t + 1];
        for j in 0..=t {
            ndp0[j] = min(dp0[j], dp1[j]);
            if j >= 1 && dp0[j - 1] < INF {
                ndp1[j] = dp0[j - 1] + c;
            }
        }
        dp0 = ndp0;
        dp1 = ndp1;
    }
    min(dp0[t], dp1[t])
}

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        if k == 0 {
            return 0;
        }
        if k > n / 2 {
            return -1;
        }
        let mut costs = vec![0i64; n];
        for i in 0..n {
            let left = nums[(i + n - 1) % n] as i64;
            let right = nums[(i + 1) % n] as i64;
            costs[i] = (left.max(right) + 1 - nums[i] as i64).max(0);
        }
        let mut best = path_dp(&costs[1..], k);
        if k >= 1 {
            let sub: &[i64] = if n > 2 { &costs[2..n - 1] } else { &[] };
            best = min(best, costs[0] + path_dp(sub, k - 1));
        }
        if best >= INF {
            -1
        } else {
            best as i32
        }
    }
}
