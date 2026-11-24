// LeetCode 3399. Smallest Substring With Identical Characters II — Hard
// https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/
// Submission 2202509352 — Accepted 970/970, Rust
//
use std::collections::VecDeque;

impl Solution {
    pub fn min_length(s: String, num_ops: i32) -> i32 {
        // My thinking: binary-search the answer L. For a fixed L,
        // the cheapest way to keep every run at most L long is a
        // left-to-right DP: the last run of the answer is one block
        // of equal characters, so the cost of ending at i with a
        // given character is the cost of that block plus the best
        // cost of the prefix before it ending in the other
        // character. The block cost is a difference of prefix
        // counts, so the best previous split is a sliding-window
        // minimum over the last L positions — two deques make the
        // whole check O(n). The deques store k = j + 1, so k = 0
        // stands for the empty prefix before the string.
        let bytes = s.as_bytes();
        let n = bytes.len();
        // nc0[i] / nc1[i]: number of '1's / '0's in s[..i].
        let mut nc0 = vec![0i32; n + 1];
        let mut nc1 = vec![0i32; n + 1];
        for i in 0..n {
            nc0[i + 1] = nc0[i] + if bytes[i] == b'1' { 1 } else { 0 };
            nc1[i + 1] = nc1[i] + if bytes[i] == b'0' { 1 } else { 0 };
        }

        fn min_flips(nc0: &[i32], nc1: &[i32], limit: usize) -> i32 {
            let n = nc0.len() - 1;
            // v0[k] = best cost of a prefix ending at k - 1 with a
            // '1', minus nc0[k]; v1 is the mirror image.
            let mut v0 = vec![0i32; n + 1];
            let mut v1 = vec![0i32; n + 1];
            let mut dq0: VecDeque<usize> = VecDeque::new();
            let mut dq1: VecDeque<usize> = VecDeque::new();
            dq0.push_back(0);
            dq1.push_back(0);
            let (mut best0, mut best1) = (0i32, 0i32);
            for i in 0..n {
                let threshold = (i + 1).saturating_sub(limit);
                while *dq0.front().unwrap() < threshold {
                    dq0.pop_front();
                }
                while *dq1.front().unwrap() < threshold {
                    dq1.pop_front();
                }
                best0 = nc0[i + 1] + v0[*dq0.front().unwrap()];
                best1 = nc1[i + 1] + v1[*dq1.front().unwrap()];
                v0[i + 1] = best1 - nc0[i + 1];
                v1[i + 1] = best0 - nc1[i + 1];
                while let Some(&k) = dq0.back() {
                    if v0[k] >= v0[i + 1] {
                        dq0.pop_back();
                    } else {
                        break;
                    }
                }
                dq0.push_back(i + 1);
                while let Some(&k) = dq1.back() {
                    if v1[k] >= v1[i + 1] {
                        dq1.pop_back();
                    } else {
                        break;
                    }
                }
                dq1.push_back(i + 1);
            }
            best0.min(best1)
        }

        let mut lo = 1usize;
        let mut hi = n;
        while lo < hi {
            let mid = (lo + hi) / 2;
            if min_flips(&nc0, &nc1, mid) <= num_ops {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        lo as i32
    }
}
