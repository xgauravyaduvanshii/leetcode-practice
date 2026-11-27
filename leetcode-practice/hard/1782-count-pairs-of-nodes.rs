// LeetCode 1782. Count Pairs Of Nodes — Hard
// https://leetcode.com/problems/count-pairs-of-nodes/
// Submission 2201161961 — Accepted, Rust
//
// My thinking: I sort the degrees and count pairs
// whose degrees add up past the query with two
// pointers, then I take back the pairs joined by an
// edge, where the shared edge was counted twice.

use std::collections::HashMap;

impl Solution {
    pub fn count_pairs(n: i32, edges: Vec<Vec<i32>>, queries: Vec<i32>) -> Vec<i32> {
        let n = n as usize;
        let mut deg = vec![0i32; n + 1];
        let mut shared: HashMap<(i32, i32), i32> = HashMap::new();
        for e in &edges {
            let (u, v) = (e[0], e[1]);
            deg[u as usize] += 1;
            deg[v as usize] += 1;
            let key = (u.min(v), u.max(v));
            *shared.entry(key).or_insert(0) += 1;
        }
        let mut degs: Vec<i32> = deg[1..].to_vec();
        degs.sort();
        let mut ans = Vec::new();
        for q in queries {
            let mut cnt: i64 = 0;
            let (mut left, mut right) = (0usize, n - 1);
            while left < right {
                if degs[left] + degs[right] > q {
                    cnt += (right - left) as i64;
                    right -= 1;
                } else {
                    left += 1;
                }
            }
            for ((u, v), c) in &shared {
                let du = deg[*u as usize];
                let dv = deg[*v as usize];
                if du + dv > q && du + dv - c <= q {
                    cnt -= 1;
                }
            }
            ans.push(cnt as i32);
        }
        ans
    }
}
