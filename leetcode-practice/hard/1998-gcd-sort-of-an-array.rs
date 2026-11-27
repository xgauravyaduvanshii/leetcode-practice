// LeetCode 1998. GCD Sort of an Array — Hard
// https://leetcode.com/problems/gcd-sort-of-an-array/
// Submission 2201300471 — Accepted, Rust
//
// My thinking: two spots can trade places exactly
// when a shared prime links them, so I join every
// index by its prime factors and check that each
// linked group already holds the right values.

use std::collections::HashMap;

struct DSU {
    parent: Vec<usize>,
}

impl DSU {
    fn new(n: usize) -> Self {
        DSU { parent: (0..n).collect() }
    }
    fn find(&mut self, x: usize) -> usize {
        if self.parent[x] != x {
            self.parent[x] = self.find(self.parent[x]);
        }
        self.parent[x]
    }
    fn union(&mut self, a: usize, b: usize) {
        let (ra, rb) = (self.find(a), self.find(b));
        if ra != rb {
            self.parent[ra] = rb;
        }
    }
}

impl Solution {
    pub fn gcd_sort(nums: Vec<i32>) -> bool {
        let n = nums.len();
        let maxv = *nums.iter().max().unwrap() as usize;
        let mut spf: Vec<usize> = (0..=maxv).collect();
        let mut i = 2;
        while i * i <= maxv {
            if spf[i] == i {
                let mut j = i * i;
                while j <= maxv {
                    if spf[j] == j {
                        spf[j] = i;
                    }
                    j += i;
                }
            }
            i += 1;
        }
        let mut dsu = DSU::new(n);
        let mut prime_to_first: HashMap<usize, usize> = HashMap::new();
        for (idx, &x) in nums.iter().enumerate() {
            let mut v = x as usize;
            let mut primes = Vec::new();
            while v > 1 {
                let p = spf[v];
                primes.push(p);
                while v % p == 0 {
                    v /= p;
                }
            }
            for p in primes {
                match prime_to_first.get(&p) {
                    Some(&first) => dsu.union(idx, first),
                    None => {
                        prime_to_first.insert(p, idx);
                    }
                }
            }
        }
        let mut groups: HashMap<usize, Vec<usize>> = HashMap::new();
        for idx in 0..n {
            let root = dsu.find(idx);
            groups.entry(root).or_default().push(idx);
        }
        let mut srt = nums.clone();
        srt.sort_unstable();
        for idxs in groups.values() {
            let mut have: Vec<i32> = idxs.iter().map(|&i| nums[i]).collect();
            let mut want: Vec<i32> = idxs.iter().map(|&i| srt[i]).collect();
            have.sort_unstable();
            want.sort_unstable();
            if have != want {
                return false;
            }
        }
        true
    }
}
