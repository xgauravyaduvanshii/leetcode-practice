// LeetCode 3859. Count Subarrays With K Distinct Integers — Hard
// https://leetcode.com/problems/count-subarrays-with-k-distinct-integers/
// Submission 2203320990 — Accepted, Rust
//
// My thinking: fix the right end r and count the left
// ends l whose window [l, r] has exactly k distinct
// values, each appearing at least m times. Two sliding
// windows give the l-range with exactly k distinct
// values: l1 is the smallest l with at most k distinct,
// l2 the smallest l with at most k - 1 distinct, so the
// distinct count is k exactly for l1 <= l < l2. A value
// v has at least m occurrences in [l, r] exactly when l
// is at or before q_v, the position of its m-th
// occurrence from the right, so the number of values
// with at least m occurrences in [l, r] reaches k
// exactly when l is at or before the k-th largest q_v
// among values seen at least m times so far. A Fenwick
// tree over positions keeps those q_v values and finds
// that k-th largest in O(log n), and the valid l for
// this r are l1 through min(l2 - 1, c), counted in O(1).
// The answer can reach about n^2 / 2, so it is i64.
use std::collections::HashMap;

struct Fenwick {
    n: usize,
    bit: Vec<i64>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Fenwick { n, bit: vec![0; n + 1] }
    }

    fn add(&mut self, mut idx: usize, delta: i64) {
        idx += 1;
        while idx <= self.n {
            self.bit[idx] += delta;
            idx += idx & idx.wrapping_neg();
        }
    }

    fn prefix(&self, mut idx: usize) -> i64 {
        idx += 1;
        let mut s = 0i64;
        while idx > 0 {
            s += self.bit[idx];
            idx -= idx & idx.wrapping_neg();
        }
        s
    }

    fn total(&self) -> i64 {
        if self.n == 0 {
            0
        } else {
            self.prefix(self.n - 1)
        }
    }

    // Smallest 0-based index whose prefix sum reaches the
    // given 1-based rank.
    fn find_kth(&self, mut rank: i64) -> usize {
        let mut idx = 0usize;
        let mut mask = 1usize;
        while mask << 1 <= self.n {
            mask <<= 1;
        }
        while mask != 0 {
            let nxt = idx + mask;
            if nxt <= self.n && self.bit[nxt] < rank {
                rank -= self.bit[nxt];
                idx = nxt;
            }
            mask >>= 1;
        }
        idx
    }
}

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32, m: i32) -> i64 {
        let n = nums.len();
        let k = k as usize;
        let m = m as usize;
        let mut fw = Fenwick::new(n);
        let mut pos: HashMap<i32, Vec<usize>> = HashMap::new();
        let mut freq1: HashMap<i32, i32> = HashMap::new();
        let mut freq2: HashMap<i32, i32> = HashMap::new();
        let mut d1 = 0i32;
        let mut d2 = 0i32;
        let mut l1 = 0usize;
        let mut l2 = 0usize;
        let mut ans: i64 = 0;
        for r in 0..n {
            let v = nums[r];
            let lst = pos.entry(v).or_default();
            lst.push(r);
            let j = lst.len();
            if j == m {
                let q = lst[0];
                fw.add(q, 1);
            } else if j > m {
                let old = lst[j - 1 - m];
                let new = lst[j - m];
                fw.add(old, -1);
                fw.add(new, 1);
            }
            let e1 = freq1.entry(v).or_insert(0);
            *e1 += 1;
            if *e1 == 1 {
                d1 += 1;
            }
            while d1 > k as i32 {
                let u = nums[l1];
                let eu = freq1.get_mut(&u).unwrap();
                *eu -= 1;
                if *eu == 0 {
                    d1 -= 1;
                }
                l1 += 1;
            }
            let e2 = freq2.entry(v).or_insert(0);
            *e2 += 1;
            if *e2 == 1 {
                d2 += 1;
            }
            while d2 > k as i32 - 1 {
                let u = nums[l2];
                let eu = freq2.get_mut(&u).unwrap();
                *eu -= 1;
                if *eu == 0 {
                    d2 -= 1;
                }
                l2 += 1;
            }
            let tot = fw.total();
            if tot >= k as i64 {
                let c = fw.find_kth(tot - k as i64 + 1) as i64;
                let hi = std::cmp::min(l2 as i64 - 1, c);
                if hi >= l1 as i64 {
                    ans += hi - l1 as i64 + 1;
                }
            }
        }
        ans
    }
}
