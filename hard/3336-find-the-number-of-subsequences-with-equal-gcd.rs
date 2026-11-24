// LeetCode 3336. Find the Number of Subsequences With Equal GCD — Hard
// https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/
// Submission 2202385848 -- Accepted, Rust
impl Solution {
    pub fn subsequence_pair_count(nums: Vec<i32>) -> i32 {
        // My thinking: I build the two disjoint subsequences element by
        // element, tracking the pair of their GCDs so far (0 means that side
        // is still empty). Each new number either is skipped, joins the
        // first subsequence (gcd(g1, a)), or joins the second (gcd(g2, a)).
        // The DP is a 201x201 grid over GCD pairs. At the end I add up the
        // counts of all pairs (g, g) with g > 0, which are exactly the pairs
        // of non-empty subsequences with equal GCD.
        const MOD: i64 = 1_000_000_007;
        const MAXV: usize = 200;
        fn gcd(mut a: i32, mut b: i32) -> usize {
            while b != 0 {
                let t = a % b;
                a = b;
                b = t;
            }
            a as usize
        }
        let mut dp = vec![vec![0i64; MAXV + 1]; MAXV + 1];
        dp[0][0] = 1;
        for &a in nums.iter() {
            let mut ndp = dp.clone();
            for g1 in 0..=MAXV {
                let ng1 = gcd(g1 as i32, a);
                for g2 in 0..=MAXV {
                    let v = dp[g1][g2];
                    if v != 0 {
                        ndp[ng1][g2] = (ndp[ng1][g2] + v) % MOD;
                        let ng2 = gcd(g2 as i32, a);
                        ndp[g1][ng2] = (ndp[g1][ng2] + v) % MOD;
                    }
                }
            }
            dp = ndp;
        }
        let mut ans = 0i64;
        for g in 1..=MAXV {
            ans = (ans + dp[g][g]) % MOD;
        }
        ans as i32
    }
}
