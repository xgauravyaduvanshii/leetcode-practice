// LeetCode 2392. Build a Matrix With Conditions — Hard
// https://leetcode.com/problems/build-a-matrix-with-conditions/
// Submission 2201715495 — Accepted, Rust
//
// My thinking: rows and columns are two
// separate orderings — I sort each one on
// its own, and if either one ties itself
// in a knot there is no matrix at all.

use std::collections::VecDeque;

impl Solution {
    pub fn build_matrix(k: i32, row_conditions: Vec<Vec<i32>>, col_conditions: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        fn topo(k: i32, conds: &[Vec<i32>]) -> Option<Vec<i32>> {
            let n = k as usize;
            let mut adj: Vec<Vec<i32>> = vec![Vec::new(); n + 1];
            let mut indeg = vec![0; n + 1];
            for c in conds {
                adj[c[0] as usize].push(c[1]);
                indeg[c[1] as usize] += 1;
            }
            let mut q: VecDeque<i32> = (1..=k).filter(|&v| indeg[v as usize] == 0).collect();
            let mut order = Vec::new();
            while let Some(u) = q.pop_front() {
                order.push(u);
                for &v in &adj[u as usize] {
                    indeg[v as usize] -= 1;
                    if indeg[v as usize] == 0 {
                        q.push_back(v);
                    }
                }
            }
            if order.len() == n { Some(order) } else { None }
        }
        let rows = match topo(k, &row_conditions) {
            Some(o) => o,
            None => return vec![],
        };
        let cols = match topo(k, &col_conditions) {
            Some(o) => o,
            None => return vec![],
        };
        let n = k as usize;
        let mut rpos = vec![0; n + 1];
        let mut cpos = vec![0; n + 1];
        for (i, &v) in rows.iter().enumerate() {
            rpos[v as usize] = i;
        }
        for (i, &v) in cols.iter().enumerate() {
            cpos[v as usize] = i;
        }
        let mut mat = vec![vec![0; n]; n];
        for v in 1..=k {
            mat[rpos[v as usize]][cpos[v as usize]] = v;
        }
        mat
    }
}
