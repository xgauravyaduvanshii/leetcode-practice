// LeetCode 2286. Booking Concert Tickets in Groups — Hard
// https://leetcode.com/problems/booking-concert-tickets-in-groups/
// Submission 2201658078 — Accepted, Rust
//
// My thinking: every row keeps its empty
// stretches in order, and a segment tree
// over the rows finds the first row with
// room — gather takes one solid block,
// scatter fills the smallest rows first.

struct BookMyShow {
    n: usize,
    m: usize,
    empty: Vec<Vec<(usize, usize)>>,
    size: usize,
    tree_max: Vec<usize>,
    tree_sum: Vec<usize>,
}

impl BookMyShow {
    fn new(n: i32, m: i32) -> Self {
        let n = n as usize;
        let m = m as usize;
        let mut size = 1usize;
        while size < n {
            size *= 2;
        }
        let mut tree_max = vec![0usize; 2 * size];
        let mut tree_sum = vec![0usize; 2 * size];
        for i in 0..n {
            tree_max[size + i] = m;
            tree_sum[size + i] = m;
        }
        for i in (1..size).rev() {
            tree_max[i] = tree_max[2 * i].max(tree_max[2 * i + 1]);
            tree_sum[i] = tree_sum[2 * i] + tree_sum[2 * i + 1];
        }
        Self {
            n,
            m,
            empty: vec![vec![(0, m - 1)]; n],
            size,
            tree_max,
            tree_sum,
        }
    }

    fn row_stats(&self, r: usize) -> (usize, usize) {
        let mut total = 0usize;
        let mut best = 0usize;
        for &(l, rr) in &self.empty[r] {
            total += rr - l + 1;
            best = best.max(rr - l + 1);
        }
        (best, total)
    }

    fn update_row(&mut self, r: usize) {
        let (best, total) = self.row_stats(r);
        let mut i = self.size + r;
        self.tree_max[i] = best;
        self.tree_sum[i] = total;
        i /= 2;
        while i > 0 {
            self.tree_max[i] = self.tree_max[2 * i].max(self.tree_max[2 * i + 1]);
            self.tree_sum[i] = self.tree_sum[2 * i] + self.tree_sum[2 * i + 1];
            i /= 2;
        }
    }

    fn range_sum(&self, l: usize, r: usize) -> usize {
        let mut l = l + self.size;
        let mut r = r + self.size;
        let mut s = 0usize;
        while l <= r {
            if l % 2 == 1 {
                s += self.tree_sum[l];
                l += 1;
            }
            if r % 2 == 0 {
                s += self.tree_sum[r];
                r -= 1;
            }
            l /= 2;
            r /= 2;
        }
        s
    }

    fn first_row_with(&self, k: usize, max_row: usize) -> Option<usize> {
        if self.tree_max[1] < k {
            return None;
        }
        let mut i = 1usize;
        let mut l = 0usize;
        let mut r = self.size - 1;
        while i < self.size {
            let left = 2 * i;
            let mid = (l + r) / 2;
            if self.tree_max[left] >= k && l <= max_row {
                i = left;
                r = mid;
            } else {
                i = left + 1;
                l = mid + 1;
            }
        }
        let row = i - self.size;
        if row > max_row || row >= self.n {
            None
        } else {
            Some(row)
        }
    }

    fn take_from_row(&mut self, r: usize, mut k: usize) -> usize {
        let mut taken = 0usize;
        while k > 0 && !self.empty[r].is_empty() {
            let (l, rr) = self.empty[r][0];
            let length = rr - l + 1;
            let take = length.min(k);
            taken += take;
            k -= take;
            if take == length {
                self.empty[r].remove(0);
            } else {
                self.empty[r][0].0 = l + take;
            }
        }
        taken
    }

    fn gather(&mut self, k: i32, max_row: i32) -> Vec<i32> {
        let k = k as usize;
        let max_row = max_row as usize;
        let r = match self.first_row_with(k, max_row) {
            Some(r) => r,
            None => return vec![],
        };
        let mut c: Option<usize> = None;
        let mut idx = 0usize;
        while idx < self.empty[r].len() {
            let (l, rr) = self.empty[r][idx];
            if rr - l + 1 >= k {
                c = Some(l);
                if rr - l + 1 == k {
                    self.empty[r].remove(idx);
                } else {
                    self.empty[r][idx].0 = l + k;
                }
                break;
            }
            idx += 1;
        }
        match c {
            Some(c) => {
                self.update_row(r);
                vec![r as i32, c as i32]
            }
            None => vec![],
        }
    }

    fn scatter(&mut self, k: i32, max_row: i32) -> bool {
        let mut k = k as usize;
        let max_row = max_row as usize;
        if self.range_sum(0, max_row) < k {
            return false;
        }
        let mut r = 0usize;
        while k > 0 {
            while r <= max_row && self.tree_sum[self.size + r] == 0 {
                r += 1;
            }
            if r > max_row {
                return false;
            }
            let taken = self.take_from_row(r, k);
            k -= taken;
            self.update_row(r);
            if k > 0 {
                r += 1;
            }
        }
        true
    }
}
