// LeetCode 2488. Count Subarrays With Median K — Hard
// https://leetcode.com/problems/count-subarrays-with-median-k/
// Submission 2201777357 — Accepted, Rust
//
// My thinking: I turn every number into
// +1 if it beats k, -1 if it loses to k,
// and 0 for k itself — a subarray holding
// k has median k exactly when its balance
// is 0 or 1, so I count how many left
// borders give each balance and sweep the
// right border past k.

use std::collections::HashMap;

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let pos = nums.iter().position(|&x| x == k).unwrap();
        let mut pref = vec![0i32; n + 1];
        for (i, &x) in nums.iter().enumerate() {
            pref[i + 1] = pref[i]
                + if x > k {
                    1
                } else if x < k {
                    -1
                } else {
                    0
                };
        }
        let mut left: HashMap<i32, i32> = HashMap::new();
        for &v in &pref[..=pos] {
            *left.entry(v).or_insert(0) += 1;
        }
        let mut ans: i32 = 0;
        for r in pos..n {
            let bal = pref[r + 1];
            ans += left.get(&bal).copied().unwrap_or(0);
            ans += left.get(&(bal - 1)).copied().unwrap_or(0);
        }
        ans
    }
}
