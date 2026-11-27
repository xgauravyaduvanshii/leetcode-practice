// LeetCode 3559. Number of Ways to Assign Edge Weights II — Hard
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/
// Submission 2202844104 — Accepted, Rust
const MOD: i64 = 1_000_000_007;

impl Solution {
    pub fn assign_edge_weights(edges: Vec<Vec<i32>>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        // My thinking: on a path of L edges, giving an edge weight 1
        // or 2, the total is odd exactly when the number of 1s is
        // odd — the 2s contribute an even amount. Summing the
        // binomial coefficients over the odd counts gives 2^(L-1)
        // (and 0 when the path is empty). So each query only needs
        // the length of the path, which I get from depths and a
        // binary-lifted lowest common ancestor.
        let n = edges.iter().map(|e| e[0].max(e[1])).max().unwrap_or(1) as usize;
        let mut adj: Vec<Vec<usize>> = vec![Vec::new(); n + 1];
        for e in &edges {
            let (u, v) = (e[0] as usize, e[1] as usize);
            adj[u].push(v);
            adj[v].push(u);
        }
        const LOG: usize = 18;
        let mut up = vec![vec![0usize; n + 1]; LOG];
        let mut depth = vec![0usize; n + 1];
        let mut parent = vec![0usize; n + 1];
        let mut order = vec![1usize];
        parent[1] = usize::MAX;
        let mut i = 0;
        while i < order.len() {
            let u = order[i];
            i += 1;
            for &v in &adj[u] {
                if parent[v] == 0 {
                    parent[v] = u;
                    depth[v] = depth[u] + 1;
                    up[0][v] = u;
                    order.push(v);
                }
            }
        }
        up[0][1] = 1;
        for k in 1..LOG {
            for v in 1..=n {
                up[k][v] = up[k - 1][up[k - 1][v]];
            }
        }
        let lca = |mut u: usize, mut v: usize| -> usize {
            if depth[u] < depth[v] {
                std::mem::swap(&mut u, &mut v);
            }
            let mut diff = depth[u] - depth[v];
            let mut bit = 0;
            while diff > 0 {
                if diff & 1 == 1 {
                    u = up[bit][u];
                }
                diff >>= 1;
                bit += 1;
            }
            if u == v {
                return u;
            }
            for k in (0..LOG).rev() {
                if up[k][u] != up[k][v] {
                    u = up[k][u];
                    v = up[k][v];
                }
            }
            up[0][u]
        };
        let mut ans = Vec::with_capacity(queries.len());
        for q in &queries {
            let (u, v) = (q[0] as usize, q[1] as usize);
            if u == v {
                ans.push(0);
                continue;
            }
            let l = depth[u] + depth[v] - 2 * depth[lca(u, v)];
            ans.push(mod_pow(2, (l - 1) as i64) as i32);
        }
        ans
    }
}

fn mod_pow(mut base: i64, mut exp: i64) -> i64 {
    let mut res = 1i64;
    while exp > 0 {
        if exp & 1 == 1 {
            res = res * base % MOD;
        }
        base = base * base % MOD;
        exp >>= 1;
    }
    res
}
