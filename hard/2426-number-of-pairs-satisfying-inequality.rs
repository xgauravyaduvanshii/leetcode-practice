// LeetCode 2426. Number of Pairs Satisfying Inequality — Hard
// https://leetcode.com/problems/number-of-pairs-satisfying-inequality/
// Submission 2201734275 — Accepted, Rust
//
// My thinking: the condition is really
// about one number per index, d[i] = a[i]
// - b[i] — I walk from the right keeping
// the differences I have seen in a
// Fenwick tree, and count how many of
// them are big enough to pair with the
// one I am on.

struct Fenwick {
    n: usize,
    bit: Vec<i64>,
}

impl Fenwick {
    fn new(n: usize) -> Self {
        Fenwick { n, bit: vec![0; n + 1] }
    }
    fn add(&mut self, mut i: usize, delta: i64) {
        i += 1;
        while i <= self.n {
            self.bit[i] += delta;
            i += i & (!i + 1);
        }
    }
    fn sum(&self, mut i: usize) -> i64 {
        let mut s = 0;
        while i > 0 {
            s += self.bit[i];
            i -= i & (!i + 1);
        }
        s
    }
}

impl Solution {
    pub fn number_of_pairs(nums1: Vec<i32>, nums2: Vec<i32>, diff: i32) -> i64 {
        let d: Vec<i64> = nums1.iter().zip(nums2.iter()).map(|(a, b)| *a as i64 - *b as i64).collect();
        let mut vals: Vec<i64> = d.clone();
        vals.sort_unstable();
        vals.dedup();
        let idx = |v: i64| -> usize { vals.binary_search(&v).unwrap() };
        let mut ft = Fenwick::new(vals.len());
        let mut ans: i64 = 0;
        let mut seen = 0i64;
        for &x in d.iter().rev() {
            let need = x - diff as i64;
            let pos = vals.partition_point(|&v| v < need);
            let less = ft.sum(pos);
            ans += seen - less;
            ft.add(idx(x), 1);
            seen += 1;
        }
        ans
    }
}
