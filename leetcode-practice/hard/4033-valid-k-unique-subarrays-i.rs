// LeetCode 4033. Valid K-Unique Subarrays I — Hard
// https://leetcode.com/problems/valid-k-unique-subarrays-i/
// Submission 2203524514 — Accepted, Rust
//
// My thinking: a subarray is valid exactly when it
// has k distinct numbers and every number in it
// occurs an even number of times. Both conditions
// are answered with prefix structures. For parity,
// give every value two independent 64-bit hashes
// (splitmix64 with different salts) and keep their
// prefix XORs: a value occurring an even number of
// times cancels itself out, so the XOR over a range
// is zero exactly when every value in the range
// occurs an even number of times. One 64-bit hash
// is not enough — a single random XOR hash collided
// on a test with 135 odd-frequency values and gave
// a false positive — so two independent hashes are
// used and both must be zero. For the distinct
// count, answer the queries offline sorted by right
// end with a Fenwick tree over last occurrences:
// scanning right, each position contributes +1 and
// its previous occurrence -1, so a range sum is the
// number of distinct values in that range.
use std::collections::HashMap;

fn splitmix64(mut x: u64) -> u64 {
    x = x.wrapping_add(0x9E3779B97F4A7C15);
    x = (x ^ (x >> 30)).wrapping_mul(0xBF58476D1CE4E5B9);
    x = (x ^ (x >> 27)).wrapping_mul(0x94D049BB133111EB);
    x ^ (x >> 31)
}

struct Fenwick {
    bit: Vec<i32>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Fenwick { bit: vec![0; n + 2] }
    }

    fn add(&mut self, mut i: usize, delta: i32) {
        i += 1;
        while i < self.bit.len() {
            self.bit[i] += delta;
            i += i & i.wrapping_neg();
        }
    }

    fn sum(&self, mut i: usize) -> i32 {
        i += 1;
        let mut s = 0;
        while i > 0 {
            s += self.bit[i];
            i -= i & i.wrapping_neg();
        }
        s
    }
}

impl Solution {
    pub fn valid_subarrays(nums: Vec<i32>, k: i32, queries: Vec<Vec<i32>>) -> Vec<bool> {
        let n = nums.len();
        let maxv = *nums.iter().max().unwrap_or(&0) as usize;
        let mut hv1 = vec![0u64; maxv + 1];
        let mut hv2 = vec![0u64; maxv + 1];
        for v in 1..=maxv {
            hv1[v] = splitmix64(v as u64 ^ 0x9E3779B97F4A7C15);
            hv2[v] = splitmix64(v as u64 ^ 0xC2B2AE3D27D4EB4F);
        }
        let mut p1 = vec![0u64; n + 1];
        let mut p2 = vec![0u64; n + 1];
        for (i, &v) in nums.iter().enumerate() {
            p1[i + 1] = p1[i] ^ hv1[v as usize];
            p2[i + 1] = p2[i] ^ hv2[v as usize];
        }

        let q = queries.len();
        let mut order: Vec<usize> = (0..q).collect();
        order.sort_by_key(|&i| queries[i][1]);
        let mut bit = Fenwick::new(n);
        let mut last: HashMap<i32, usize> = HashMap::new();
        let mut distinct = vec![0i32; q];
        let mut cur = 0usize;
        for &qi in &order {
            let (l, r) = (queries[qi][0] as usize, queries[qi][1] as usize);
            while cur <= r {
                let v = nums[cur];
                if let Some(&prev) = last.get(&v) {
                    bit.add(prev, -1);
                }
                bit.add(cur, 1);
                last.insert(v, cur);
                cur += 1;
            }
            distinct[qi] = bit.sum(r) - if l > 0 { bit.sum(l - 1) } else { 0 };
        }

        queries
            .iter()
            .enumerate()
            .map(|(i, qr)| {
                let (l, r) = (qr[0] as usize, qr[1] as usize);
                distinct[i] == k && (p1[r + 1] ^ p1[l]) == 0 && (p2[r + 1] ^ p2[l]) == 0
            })
            .collect()
    }
}
