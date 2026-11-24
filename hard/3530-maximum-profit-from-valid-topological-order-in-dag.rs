// LeetCode 3530. Maximum Profit from Valid Topological Order in DAG — Hard
// https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag/
// Submission 2202805415 — Accepted, Rust
impl Solution {
    pub fn max_profit(n: i32, edges: Vec<Vec<i32>>, score: Vec<i32>) -> i32 {
        // My thinking: n is at most 22, so I enumerate which nodes
        // have been placed as a bitmask. dp[mask] is the best profit
        // for placing exactly those nodes in the first popcount(mask)
        // positions; from a mask I may place any node whose
        // prerequisites are all already placed, and it earns
        // score[v] times its (1-based) position. The best order is
        // dp over the full mask.
        let n = n as usize;
        let mut pre = vec![0u32; n];
        for e in &edges {
            pre[e[1] as usize] |= 1u32 << e[0];
        }
        let total = 1usize << n;
        let neg: i64 = -1_000_000_000_000_000_000;
        let mut dp = vec![neg; total];
        dp[0] = 0;
        for mask in 0..total {
            if dp[mask] == neg {
                continue;
            }
            let pos = (mask.count_ones() + 1) as i64;
            for v in 0..n {
                if mask & (1usize << v) != 0 {
                    continue;
                }
                if (mask as u32) & pre[v] != pre[v] {
                    continue;
                }
                let nmask = mask | (1usize << v);
                let val = dp[mask] + score[v] as i64 * pos;
                if val > dp[nmask] {
                    dp[nmask] = val;
                }
            }
        }
        dp[total - 1] as i32
    }
}
