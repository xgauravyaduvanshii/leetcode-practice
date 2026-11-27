// LeetCode 2608. Shortest Cycle in a Graph — Hard
// https://leetcode.com/problems/shortest-cycle-in-a-graph/
// Submission 2201848894 — Accepted, Rust
//
// My thinking: I walk out from every
// vertex in turn, and the first time a
// walk meets a vertex it has already
// reached by another road, the two roads
// together close a cycle — the shortest
// such meeting anywhere is the answer.

use std::collections::VecDeque;

impl Solution {
    pub fn find_shortest_cycle(n: i32, edges: Vec<Vec<i32>>) -> i32 {
        let n = n as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n];
        for e in &edges {
            let (a, b) = (e[0] as usize, e[1] as usize);
            adj[a].push(b);
            adj[b].push(a);
        }
        let mut best = i32::MAX;
        for s in 0..n {
            let mut dist = vec![-1i32; n];
            let mut parent = vec![-1i32; n];
            dist[s] = 0;
            let mut q = VecDeque::new();
            q.push_back(s);
            while let Some(u) = q.pop_front() {
                for &v in &adj[u] {
                    if dist[v] == -1 {
                        dist[v] = dist[u] + 1;
                        parent[v] = u as i32;
                        q.push_back(v);
                    } else if parent[u] != v as i32 && parent[v] != u as i32 {
                        best = best.min(dist[u] + dist[v] + 1);
                    }
                }
            }
        }
        if best == i32::MAX {
            -1
        } else {
            best
        }
    }
}
