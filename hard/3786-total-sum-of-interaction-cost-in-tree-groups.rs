// LeetCode 3786. Total Sum of Interaction Cost in Tree Groups — Hard
// https://leetcode.com/problems/total-sum-of-interaction-cost-in-tree-groups/
// Submission 2203179789 — Accepted, Rust
impl Solution {
    pub fn interaction_costs(n: i32, edges: Vec<Vec<i32>>, group: Vec<i32>) -> i64 {
        // My thinking: the distance between two same-group nodes
        // is the number of tree edges on their path, so each edge
        // contributes once for every same-group pair whose path
        // crosses it. Root the tree at 0: for the edge down to a
        // child subtree, a group with cnt nodes inside the
        // subtree and total - cnt outside contributes
        // cnt * (total - cnt). There are only 20 groups, so one
        // bottom-up pass keeps a 21-wide count array per
        // subtree and adds each edge's contribution directly.
        let n = n as usize;
        let mut adj = vec![Vec::new(); n];
        for e in &edges {
            let (u, v) = (e[0] as usize, e[1] as usize);
            adj[u].push(v);
            adj[v].push(u);
        }
        let mut total = [0i64; 21];
        for &g in &group {
            total[g as usize] += 1;
        }
        // Root the tree at 0 with an explicit stack; parent[0]
        // is 0 itself so the root is never pushed twice.
        let mut parent = vec![usize::MAX; n];
        parent[0] = 0;
        let mut order = Vec::with_capacity(n);
        let mut stack = vec![0usize];
        while let Some(u) = stack.pop() {
            order.push(u);
            for &v in &adj[u] {
                if parent[v] == usize::MAX {
                    parent[v] = u;
                    stack.push(v);
                }
            }
        }
        let mut sub = vec![[0i64; 21]; n];
        let mut ans: i64 = 0;
        for &u in order.iter().rev() {
            for &v in &adj[u] {
                if parent[v] == u {
                    let cv = sub[v];
                    for g in 1..21 {
                        sub[u][g] += cv[g];
                        ans += cv[g] * (total[g] - cv[g]);
                    }
                }
            }
            sub[u][group[u] as usize] += 1;
        }
        ans
    }
}
