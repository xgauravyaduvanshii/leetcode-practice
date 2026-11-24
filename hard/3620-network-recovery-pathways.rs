// LeetCode 3620. Network Recovery Pathways — Hard
// https://leetcode.com/problems/network-recovery-pathways/
// Submission 2202883458 — Accepted, Rust
use std::collections::VecDeque;

impl Solution {
    pub fn find_max_path_score(edges: Vec<Vec<i32>>, online: Vec<bool>, k: i64) -> i32 {
        // My thinking: the answer is the largest minimum edge cost
        // over valid paths, so I binary search that value. For a
        // trial value X I keep only edges costing at least X and
        // ask whether a path from 0 to n-1 through online nodes
        // costs at most k in total. Because the graph is a DAG, that
        // check is a single pass in topological order, which keeps
        // the whole search cheap.
        let n = online.len();
        let mut adj: Vec<Vec<(usize, i64)>> = vec![Vec::new(); n];
        let mut indeg = vec![0usize; n];
        for e in &edges {
            let (u, v, c) = (e[0] as usize, e[1] as usize, e[2] as i64);
            adj[u].push((v, c));
            indeg[v] += 1;
        }
        let mut dq = VecDeque::new();
        for i in 0..n {
            if indeg[i] == 0 {
                dq.push_back(i);
            }
        }
        let mut topo = Vec::with_capacity(n);
        while let Some(u) = dq.pop_front() {
            topo.push(u);
            for &(v, _) in &adj[u] {
                indeg[v] -= 1;
                if indeg[v] == 0 {
                    dq.push_back(v);
                }
            }
        }
        let mut costs: Vec<i64> = edges.iter().map(|e| e[2] as i64).collect();
        costs.sort();
        costs.dedup();
        let inf = i64::MAX / 4;
        let can = |x: i64| -> bool {
            let mut dist = vec![inf; n];
            dist[0] = 0;
            for &u in &topo {
                if dist[u] == inf {
                    continue;
                }
                if u != 0 && u != n - 1 && !online[u] {
                    continue;
                }
                for &(v, c) in &adj[u] {
                    if c < x {
                        continue;
                    }
                    if v != 0 && v != n - 1 && !online[v] {
                        continue;
                    }
                    if dist[u] + c < dist[v] {
                        dist[v] = dist[u] + c;
                    }
                }
            }
            dist[n - 1] <= k
        };
        if !can(0) {
            return -1;
        }
        let mut lo = 0i32;
        let mut hi = costs.len() as i32 - 1;
        let mut best: i64 = 0;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if can(costs[mid as usize]) {
                best = costs[mid as usize];
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        best as i32
    }
}
