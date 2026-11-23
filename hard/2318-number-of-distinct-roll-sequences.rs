// LeetCode 2318. Number of Distinct Roll Sequences — Hard
// https://leetcode.com/problems/number-of-distinct-roll-sequences/
// Submission 2201674863 — Accepted, Rust
//
// My thinking: only the last two rolls
// matter — the next one must be coprime
// with the last and different from both —
// so I count how many ways each pair of
// last rolls can arise and grow them.

const MOD: i64 = 1_000_000_007;

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

impl Solution {
    pub fn distinct_sequences(n: i32) -> i32 {
        if n == 1 {
            return 6;
        }
        let mut dp = [[0i64; 7]; 7];
        for a in 1..7 {
            for b in 1..7 {
                if a != b && gcd(a, b) == 1 {
                    dp[a as usize][b as usize] = 1;
                }
            }
        }
        for _ in 3..=n {
            let mut ndp = [[0i64; 7]; 7];
            for a in 1..7 {
                for b in 1..7 {
                    let cur = dp[a as usize][b as usize];
                    if cur == 0 {
                        continue;
                    }
                    for c in 1..7 {
                        if c != a && c != b && gcd(b, c) == 1 {
                            ndp[b as usize][c as usize] = (ndp[b as usize][c as usize] + cur) % MOD;
                        }
                    }
                }
            }
            dp = ndp;
        }
        let mut total = 0i64;
        for a in 1..7 {
            for b in 1..7 {
                total = (total + dp[a as usize][b as usize]) % MOD;
            }
        }
        total as i32
    }
}
