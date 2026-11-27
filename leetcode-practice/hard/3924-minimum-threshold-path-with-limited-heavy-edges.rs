// LeetCode 3924. Minimum Threshold Path With Limited Heavy Edges — Hard
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/
// Submission 2203407395 — Accepted, Rust
use std::collections::VecDeque;

impl Solution {
    pub fn minimum_threshold(n: i32, edges: Vec<Vec<i32>>, source: i32, target: i32, k: i32) -> i32 {
        // My thinking: for a fixed threshold T an edge is
        // heavy exactly when its weight is above T, so a
        // path is valid when it uses at most k heavy edges.
        // That is a shortest path in a 0-1 graph — light
        // edges cost 0, heavy edges cost 1 — solved with
        // a 0-1 BFS. Validity is monotone in T: raising
        // the threshold only turns heavy edges light, so
        // the smallest valid threshold is found by binary
        // search over the candidate values 0 and the
        // distinct edge weights (nothing changes between
        // consecutive weights). If even the largest weight
        // fails, the target is unreachable and the answer
        // is -1. Source equal to target needs no edges,
        // so threshold 0 works.
        let n = n as usize;
        let source = source as usize;
        let target = target as usize;
        let mut adj: Vec<Vec<(usize, i32)>> = vec![Vec::new(); n];
        for e in &edges {
            let (u, v, w) = (e[0] as usize, e[1] as usize, e[2]);
            adj[u].push((v, w));
            adj[v].push((u, w));
        }
        let valid = |threshold: i32| -> bool {
            let inf = i32::MAX / 2;
            let mut dist = vec![inf; n];
            dist[source] = 0;
            let mut dq: VecDeque<usize> = VecDeque::new();
            dq.push_back(source);
            while let Some(u) = dq.pop_front() {
                for &(v, w) in &adj[u] {
                    let c = if w > threshold { 1 } else { 0 };
                    if dist[u] + c < dist[v] {
                        dist[v] = dist[u] + c;
                        if c == 0 {
                            dq.push_front(v);
                        } else {
                            dq.push_back(v);
                        }
                    }
                }
            }
            dist[target] <= k
        };
        let mut candidates: Vec<i32> = edges.iter().map(|e| e[2]).collect();
        candidates.push(0);
        candidates.sort_unstable();
        candidates.dedup();
        if !valid(*candidates.last().unwrap()) {
            return -1;
        }
        let (mut lo, mut hi) = (0usize, candidates.len() - 1);
        while lo < hi {
            let mid = (lo + hi) / 2;
            if valid(candidates[mid]) {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        candidates[lo]
    }
}
