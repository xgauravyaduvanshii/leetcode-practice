// LeetCode 1751. Maximum Number of Events That Can Be Attended II — Hard
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/
// Submission 2201141281 — Accepted, Rust
//
// My thinking: I sort the events by start time and
// walk backwards keeping, for each number of events
// I may still attend, the best value from here on —
// taking an event jumps straight to the first event
// that starts after it ends.

impl Solution {
    pub fn max_value(mut events: Vec<Vec<i32>>, k: i32) -> i32 {
        events.sort_by_key(|e| e[0]);
        let n = events.len();
        let starts: Vec<i32> = events.iter().map(|e| e[0]).collect();
        let mut nxt = vec![n; n];
        for i in 0..n {
            let mut lo = i + 1;
            let mut hi = n;
            while lo < hi {
                let mid = (lo + hi) / 2;
                if starts[mid] <= events[i][1] {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            nxt[i] = lo;
        }
        let k = k as usize;
        let mut prev = vec![0; n + 1];
        for _ in 0..k {
            let mut curr = vec![0; n + 1];
            for i in (0..n).rev() {
                curr[i] = curr[i + 1].max(events[i][2] + prev[nxt[i]]);
            }
            prev = curr;
        }
        prev[0]
    }
}
