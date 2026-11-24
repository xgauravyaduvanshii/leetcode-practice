// LeetCode 3454. Separate Squares II — Hard
// https://leetcode.com/problems/separate-squares-ii/
// Submission 2202550182 — Accepted 763/763, Rust
use std::collections::BTreeSet;

struct SegTree {
    xs: Vec<i64>,
    cnt: Vec<i32>,
    covered: Vec<i64>,
}

impl SegTree {
    fn new(xs: Vec<i64>) -> Self {
        let n = xs.len().saturating_sub(1).max(1);
        SegTree {
            xs,
            cnt: vec![0; 4 * n],
            covered: vec![0; 4 * n],
        }
    }

    fn update(&mut self, node: usize, lo: usize, hi: usize, ql: usize, qr: usize, val: i32) {
        if ql > hi || qr < lo {
            return;
        }
        if ql <= lo && hi <= qr {
            self.cnt[node] += val;
        } else {
            let mid = (lo + hi) / 2;
            self.update(node * 2, lo, mid, ql, qr, val);
            self.update(node * 2 + 1, mid + 1, hi, ql, qr, val);
        }
        if self.cnt[node] > 0 {
            self.covered[node] = self.xs[hi + 1] - self.xs[lo];
        } else if lo == hi {
            self.covered[node] = 0;
        } else {
            self.covered[node] = self.covered[node * 2] + self.covered[node * 2 + 1];
        }
    }

    fn total(&self) -> i64 {
        self.covered[1]
    }
}

impl Solution {
    pub fn separate_squares(squares: Vec<Vec<i32>>) -> f64 {
        // My thinking: sweep a horizontal line upward, keeping
        // the total covered x-length in a segment tree over the
        // compressed x-coordinates, so each strip between two
        // event y's has a known width and area. The first strip
        // whose area reaches half the total union area holds the
        // answer, found by exact integer arithmetic and a single
        // linear interpolation inside that strip.
        let mut xset = BTreeSet::new();
        for sq in &squares {
            xset.insert(sq[0] as i64);
            xset.insert(sq[0] as i64 + sq[2] as i64);
        }
        let xs: Vec<i64> = xset.into_iter().collect();
        let n = xs.len() - 1;
        let mut events: Vec<(i64, i32, i64, i64)> = Vec::new();
        for sq in &squares {
            let (x, y, l) = (sq[0] as i64, sq[1] as i64, sq[2] as i64);
            events.push((y, 1, x, x + l));
            events.push((y + l, -1, x, x + l));
        }
        events.sort();
        let mut tree = SegTree::new(xs.clone());
        let mut stages: Vec<(i64, i64, i64)> = Vec::new();
        let mut total: i64 = 0;
        for i in 0..events.len() - 1 {
            let (y, delta, x1, x2) = events[i];
            let l = xs.binary_search(&x1).unwrap();
            let r = xs.binary_search(&x2).unwrap() - 1;
            tree.update(1, 0, n - 1, l, r, delta);
            let width = tree.total();
            let height = events[i + 1].0 - y;
            total += height * width;
            stages.push((y, width, events[i + 1].0));
        }
        let mut below: i64 = 0;
        for (y0, width, y1) in stages {
            let area = (y1 - y0) * width;
            if 2 * (below + area) >= total {
                if width == 0 {
                    return y0 as f64;
                }
                return y0 as f64 + (total - 2 * below) as f64 / (2 * width) as f64;
            }
            below += area;
        }
        events[events.len() - 1].0 as f64
    }
}
