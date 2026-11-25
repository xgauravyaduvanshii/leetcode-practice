// LeetCode 3651. Minimum Cost Path with Teleportations — Hard
// https://leetcode.com/problems/minimum-cost-path-with-teleportations/
// Submission 2202930968 — Accepted, Rust
impl Solution {
    pub fn min_cost(grid: Vec<Vec<i32>>, k: i32) -> i32 {
        // My thinking: I keep a table of the cheapest cost to
        // reach every cell with a given number of teleports used.
        // With no teleports it is the plain walk down/right, adding
        // the cell I step onto. One more teleport can land me on
        // any cell whose value is no bigger than the value of the
        // cell I teleport from, for free — so for each value I only
        // need the cheapest cost to reach any cell of that value
        // or higher, which is a suffix minimum over the values.
        // After landing I walk again, so each layer is one
        // teleport plus one plain walk, and I repeat it k times.
        let m = grid.len();
        let n = grid[0].len();
        let inf = i64::MAX / 4;
        let mut dp = vec![vec![0i64; n]; m];
        for i in 0..m {
            for j in 0..n {
                dp[i][j] = if i == 0 && j == 0 {
                    0
                } else if i == 0 {
                    dp[i][j - 1] + grid[i][j] as i64
                } else if j == 0 {
                    dp[i - 1][j] + grid[i][j] as i64
                } else {
                    dp[i - 1][j].min(dp[i][j - 1]) + grid[i][j] as i64
                };
            }
        }
        let max_v = grid.iter().flatten().max().copied().unwrap_or(0) as usize;
        for _ in 0..k {
            let mut best = vec![inf; max_v + 1];
            for i in 0..m {
                for j in 0..n {
                    let v = grid[i][j] as usize;
                    if dp[i][j] < best[v] {
                        best[v] = dp[i][j];
                    }
                }
            }
            let mut suff = vec![inf; max_v + 2];
            for v in (0..=max_v).rev() {
                suff[v] = best[v].min(suff[v + 1]);
            }
            let mut ndp = vec![vec![0i64; n]; m];
            for i in 0..m {
                for j in 0..n {
                    let mut c = suff[grid[i][j] as usize];
                    if i > 0 {
                        c = c.min(ndp[i - 1][j] + grid[i][j] as i64);
                    }
                    if j > 0 {
                        c = c.min(ndp[i][j - 1] + grid[i][j] as i64);
                    }
                    ndp[i][j] = c;
                }
            }
            dp = ndp;
        }
        dp[m - 1][n - 1] as i32
    }
}
