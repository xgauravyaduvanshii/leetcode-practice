// LeetCode 3590. Kth Smallest Path XOR Sum — Hard
// https://leetcode.com/problems/kth-smallest-path-xor-sum/
// Submission 2202864304 — Accepted, Rust
use std::collections::HashMap;

impl Solution {
    pub fn kth_smallest(par: Vec<i32>, vals: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i32> {
        // My thinking: the path XOR to a node is the XOR of the
        // values on the root path, so each subtree just needs the
        // sorted list of the distinct path XORs inside it. I build
        // those lists bottom-up, always merging the smaller list
        // into the larger one, and answer each query by indexing
        // straight into its node's sorted list.
        let n = vals.len();
        let mut children: Vec<Vec<usize>> = vec![Vec::new(); n];
        for i in 1..n {
            children[par[i] as usize].push(i);
        }
        let mut pref = vec![0i32; n];
        pref[0] = vals[0];
        let mut order = vec![0usize];
        let mut i = 0;
        while i < order.len() {
            let u = order[i];
            i += 1;
            for &v in &children[u] {
                pref[v] = pref[u] ^ vals[v];
                order.push(v);
            }
        }
        let mut q_by_node: HashMap<usize, Vec<(usize, usize)>> = HashMap::new();
        for (qi, q) in queries.iter().enumerate() {
            q_by_node.entry(q[0] as usize).or_default().push((qi, q[1] as usize));
        }
        let mut ans = vec![-1i32; queries.len()];
        fn dfs(
            u: usize,
            children: &Vec<Vec<usize>>,
            pref: &Vec<i32>,
            q_by_node: &HashMap<usize, Vec<(usize, usize)>>,
            ans: &mut Vec<i32>,
        ) -> Vec<i32> {
            let mut best: Vec<i32> = Vec::new();
            for &v in &children[u] {
                let lst = dfs(v, children, pref, q_by_node, ans);
                if best.is_empty() {
                    best = lst;
                    continue;
                }
                let (big, small) = if lst.len() > best.len() { (lst, best) } else { (best, lst) };
                let mut merged: Vec<i32> = Vec::with_capacity(big.len() + small.len());
                let (mut a, mut b) = (0usize, 0usize);
                while a < big.len() && b < small.len() {
                    if big[a] < small[b] {
                        merged.push(big[a]);
                        a += 1;
                    } else if big[a] > small[b] {
                        merged.push(small[b]);
                        b += 1;
                    } else {
                        merged.push(big[a]);
                        a += 1;
                        b += 1;
                    }
                }
                merged.extend_from_slice(&big[a..]);
                merged.extend_from_slice(&small[b..]);
                best = merged;
            }
            match best.binary_search(&pref[u]) {
                Ok(_) => {}
                Err(idx) => {
                    best.insert(idx, pref[u]);
                }
            }
            if let Some(qs) = q_by_node.get(&u) {
                for &(qi, k) in qs {
                    if k <= best.len() {
                        ans[qi] = best[k - 1];
                    }
                }
            }
            best
        }
        dfs(0, &children, &pref, &q_by_node, &mut ans);
        ans
    }
}
