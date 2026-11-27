impl Solution {
    pub fn num_of_arrays(n: i32, m: i32, k: i32) -> i32 {
        // My thinking: build the array left to right, tracking
        // the biggest value seen and how many times it changed
        // — each new value either stays under the maximum or
        // raises it.
        const MOD: i64 = 1_000_000_007;
        let m = m as usize;
        let k = k as usize;
        if k == 0 {
            return 0;
        }
        let mut dp = vec![vec![0i64; k + 1]; m + 1];
        for v in 1..=m {
            dp[v][1] = 1;
        }
        for _ in 1..n {
            let mut new = vec![vec![0i64; k + 1]; m + 1];
            for c in 1..=k {
                let mut prefix: i64 = 0;
                for v in 1..=m {
                    new[v][c] = (new[v][c] + dp[v][c] * v as i64) % MOD;
                    if c < k {
                        new[v][c + 1] = (new[v][c + 1] + prefix) % MOD;
                    }
                    prefix = (prefix + dp[v][c]) % MOD;
                }
            }
            dp = new;
        }
        let mut total: i64 = 0;
        for v in 1..=m {
            total = (total + dp[v][k]) % MOD;
        }
        total as i32
    }
}
