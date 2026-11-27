// LeetCode 1825. Finding MK Average — Hard
// https://leetcode.com/problems/finding-mk-average/
// Submission 2201186215 — Accepted, Rust
//
// My thinking: I keep the last m numbers in two
// Fenwick trees — one for how many of each value
// there are, one for their sums — so the average
// of the middle part is just the sum of the
// smallest m-k values minus the sum of the
// smallest k values.

use std::collections::VecDeque;

struct BIT {
    n: usize,
    bit: Vec<i64>,
}

impl BIT {
    fn new(n: usize) -> Self {
        BIT { n, bit: vec![0; n + 1] }
    }

    fn add(&mut self, mut i: usize, delta: i64) {
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

    fn kth(&self, mut k: i64) -> usize {
        let mut idx = 0usize;
        let mut bit = 1usize;
        while bit * 2 <= self.n {
            bit *= 2;
        }
        while bit > 0 {
            let nxt = idx + bit;
            if nxt <= self.n && self.bit[nxt] < k {
                k -= self.bit[nxt];
                idx = nxt;
            }
            bit /= 2;
        }
        idx + 1
    }
}

struct MKAverage {
    m: usize,
    k: usize,
    window: VecDeque<i64>,
    cnt: BIT,
    sums: BIT,
}

impl MKAverage {
    fn new(m: i32, k: i32) -> Self {
        MKAverage {
            m: m as usize,
            k: k as usize,
            window: VecDeque::new(),
            cnt: BIT::new(100000),
            sums: BIT::new(100000),
        }
    }

    fn add_element(&mut self, num: i32) {
        let num = num as i64;
        self.window.push_back(num);
        self.cnt.add(num as usize, 1);
        self.sums.add(num as usize, num);
        if self.window.len() > self.m {
            let old = self.window.pop_front().unwrap();
            self.cnt.add(old as usize, -1);
            self.sums.add(old as usize, -old);
        }
    }

    fn calculate_mk_average(&self) -> i32 {
        if self.window.len() < self.m {
            return -1;
        }
        let mid = self.sum_smallest(self.m - self.k) - self.sum_smallest(self.k);
        (mid / (self.m - 2 * self.k) as i64) as i32
    }

    fn sum_smallest(&self, t: usize) -> i64 {
        if t == 0 {
            return 0;
        }
        let v = self.cnt.kth(t as i64);
        let c = self.cnt.sum(v - 1);
        let s = self.sums.sum(v - 1);
        s + (t as i64 - c) * v as i64
    }
}
