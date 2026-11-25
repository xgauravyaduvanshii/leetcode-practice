// LeetCode 3757. Number of Effective Subsequences — Hard
// https://leetcode.com/problems/number-of-effective-subsequences/
// Submission 2203161140 — Accepted, Rust
impl Solution {
    pub fn count_effective(nums: Vec<i32>) -> i32 {
        // My thinking: a subsequence is effective exactly when
        // removing it kills at least one bit of the total OR.
        // For each bit b of the total OR, let E_b be the event
        // that the subsequence contains every element carrying
        // b — then the subsequence is effective exactly when at
        // least one E_b happens. By inclusion-exclusion over
        // the bits, the count of subsequences where a chosen
        // set U of events all happen is 2 raised to the number
        // of elements carrying none of U's bits. Compressing
        // each number to its mask over the total OR's bits
        // (at most 20), a SOS DP over the 2^k masks counts,
        // for every mask, how many elements sit inside it, and
        // the signed sum over all masks gives the number of
        // non-effective subsequences; the answer is 2^n minus
        // that, modulo 1e9 + 7.
        const MOD: i64 = 1_000_000_007;
        let mut total_or = 0i32;
        for &x in &nums {
            total_or |= x;
        }
        let bits: Vec<i32> = (0..20).filter(|&b| (total_or >> b) & 1 == 1).collect();
        let k = bits.len();
        let n = nums.len();
        let m = 1usize << k;
        let mut h = vec![0i64; m];
        for &x in &nums {
            let mut mask = 0usize;
            for (j, &b) in bits.iter().enumerate() {
                if (x >> b) & 1 == 1 {
                    mask |= 1 << j;
                }
            }
            h[mask] += 1;
        }
        for j in 0..k {
            for mask in 0..m {
                if mask & (1 << j) != 0 {
                    h[mask] += h[mask ^ (1 << j)];
                }
            }
        }
        let mut pow2 = vec![0i64; n + 1];
        pow2[0] = 1;
        for i in 1..=n {
            pow2[i] = (pow2[i - 1] * 2) % MOD;
        }
        // The signed sum stays within about 1e15, safe in i64.
        let mut total: i64 = 0;
        for mask in 0..m {
            let pc = (mask as u32).count_ones() as usize;
            let term = pow2[h[mask] as usize];
            if (k - pc) % 2 == 0 {
                total += term;
            } else {
                total -= term;
            }
        }
        (((pow2[n] - total) % MOD + MOD) % MOD) as i32
    }
}
