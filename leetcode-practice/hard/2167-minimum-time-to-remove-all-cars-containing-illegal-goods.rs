// LeetCode 2167. Minimum Time to Remove All Cars Containing Illegal Goods — Hard
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/
// Submission 2201598865 — Accepted, Rust
//
// My thinking: the cars in the middle are
// cheapest pulled out where they stand at two
// a piece, while the ends come off one a
// piece — so I keep a middle stretch, pay the
// ends to reach it, and let the cheapest
// left-hand start win as the stretch grows.

impl Solution {
    pub fn minimum_time(s: String) -> i32 {
        let chars: Vec<char> = s.chars().collect();
        let n = chars.len();
        let ones: Vec<usize> = (0..n).filter(|&i| chars[i] == '1').collect();
        if ones.is_empty() {
            return 0;
        }
        let mut prefix = vec![0i32; n + 1];
        for i in 0..n {
            prefix[i + 1] = prefix[i] + if chars[i] == '1' { 1 } else { 0 };
        }
        let mut best = 2 * ones.len() as i32;
        let mut min_left = 0i32;
        for r in 0..n {
            min_left = min_left.min(r as i32 - 2 * prefix[r]);
            let cost = min_left + (n - 1 - r) as i32 + 2 * prefix[r + 1];
            best = best.min(cost);
        }
        best = best.min(*ones.last().unwrap() as i32 + 1);
        best = best.min((n - ones[0]) as i32);
        best
    }
}
