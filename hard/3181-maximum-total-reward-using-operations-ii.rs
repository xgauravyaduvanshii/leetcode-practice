// LeetCode 3181. Maximum Total Reward Using Operations II — Hard
// https://leetcode.com/problems/maximum-total-reward-using-operations-ii/
// Submission 2202066259 — Accepted, Rust
//
// My thinking: a total x is reachable
// when some reward v can be taken from a
// total below v. I track reachable totals
// as a bitset of 64-bit words: for each
// distinct v, the new totals are the old
// totals below v shifted by v, with
// everything at or above 2v masked off.
// The answer is the highest set bit.

struct Solution;

impl Solution {
    pub fn max_total_reward(reward_values: Vec<i32>) -> i32 {
        let mut vals: Vec<i32> = reward_values;
        vals.sort_unstable();
        vals.dedup();
        let max_v = *vals.iter().max().unwrap_or(&0) as usize;
        let limit = 2 * max_v;
        let w = (limit + 64) / 64;
        let mut dp = vec![0u64; w];
        if w > 0 {
            dp[0] = 1;
        }
        let mut shifted = vec![0u64; w];
        for &vv in &vals {
            let v = vv as usize;
            for x in shifted.iter_mut() {
                *x = 0;
            }
            let word_shift = v / 64;
            let bit_shift = v % 64;
            for i in (0..w).rev() {
                let mut val = 0u64;
                if i >= word_shift {
                    val = dp[i - word_shift] << bit_shift;
                    if bit_shift != 0 && i - word_shift > 0 {
                        val |= dp[i - word_shift - 1] >> (64 - bit_shift);
                    }
                }
                shifted[i] = val;
            }
            let max_bit = 2 * v;
            let word_idx = max_bit / 64;
            let bit_idx = max_bit % 64;
            if word_idx < w {
                if bit_idx == 0 {
                    for i in word_idx..w {
                        shifted[i] = 0;
                    }
                } else {
                    shifted[word_idx] &= (1u64 << bit_idx) - 1;
                    for i in word_idx + 1..w {
                        shifted[i] = 0;
                    }
                }
            }
            for i in 0..w {
                dp[i] |= shifted[i];
            }
        }
        for i in (0..w).rev() {
            if dp[i] != 0 {
                return (i * 64 + (63 - dp[i].leading_zeros() as usize)) as i32;
            }
        }
        0
    }
}
