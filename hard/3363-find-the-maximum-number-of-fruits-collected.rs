// LeetCode 3363. Find the Maximum Number of Fruits Collected — Hard
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/
// Submission 2202426142 -- Accepted, Rust
impl Solution {
    pub fn max_collected_fruits(fruits: Vec<Vec<i32>>) -> i32 {
        // My thinking: the child from (0,0) must move diagonally every time
        // to reach (n-1,n-1) in n-1 moves, so it takes the whole main
        // diagonal. The child from (0,n-1) can never go below the diagonal
        // (once below, its column can never catch up to its row in time to
        // reach (n-1,n-1)), and the child from (n-1,0) can never go above
        // it, so the two collect from disjoint regions except the diagonal,
        // which is already taken. I run a DP for each of them with diagonal
        // cells worth zero.
        const NEG: i64 = -1_000_000_000_000_000_000;
        let n = fruits.len();
        let diag: i64 = (0..n).map(|i| fruits[i][i] as i64).sum();
        // child 2: from (0, n-1), moves (1,-1), (1,0), (1,1); region i <= j
        let mut dp = vec![vec![NEG; n]; n];
        dp[0][n - 1] = fruits[0][n - 1] as i64;
        for i in 1..n {
            for j in i..n {
                let mut best = NEG;
                let lo = j.saturating_sub(1);
                let hi = (j + 1).min(n - 1);
                for pj in lo..=hi {
                    if dp[i - 1][pj] != NEG {
                        best = best.max(dp[i - 1][pj]);
                    }
                }
                if best != NEG {
                    dp[i][j] = best + if i == j { 0 } else { fruits[i][j] as i64 };
                }
            }
        }
        let child2 = dp[n - 1][n - 1];
        // child 3: from (n-1, 0), moves (-1,1), (0,1), (1,1); region i >= j
        let mut dp = vec![vec![NEG; n]; n];
        dp[n - 1][0] = fruits[n - 1][0] as i64;
        for j in 1..n {
            for i in j..n {
                let mut best = NEG;
                let lo = i.saturating_sub(1);
                let hi = (i + 1).min(n - 1);
                for pi in lo..=hi {
                    if dp[pi][j - 1] != NEG {
                        best = best.max(dp[pi][j - 1]);
                    }
                }
                if best != NEG {
                    dp[i][j] = best + if i == j { 0 } else { fruits[i][j] as i64 };
                }
            }
        }
        let child3 = dp[n - 1][n - 1];
        (diag + child2 + child3) as i32
    }
}
