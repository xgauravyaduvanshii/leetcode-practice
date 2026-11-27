// LeetCode 3721. Longest Balanced Subarray II — Hard
// https://leetcode.com/problems/longest-balanced-subarray-ii/
// Submission 2203065688 — Accepted, Rust
//
// My thinking: give every distinct value a sign, +1 for odd
// and -1 for even, so a subarray is balanced exactly when the
// signs of its distinct values sum to zero. Fix the right
// end r and keep, for every possible left end l, the balance
// of nums[l..r]. When r moves one step right to a value seen
// before at p, only the starts l in (p, r] gain a newly
// distinct value — the starts at or before p already contain
// it — so that step is one range add of the sign over
// [p+1, r]. The longest balanced subarray ending at r then
// starts at the smallest l whose balance is zero, and the
// answer is the best of those over all r. A lazy segment
// tree holds the balances and finds that leftmost zero in
// O(log n) per step.
use std::collections::HashMap;

struct SegTree {
    mn: Vec<i32>,
    mx: Vec<i32>,
    add: Vec<i32>,
}

impl SegTree {
    fn new(n: usize) -> Self {
        let size = 4 * n.max(1);
        SegTree {
            mn: vec![0; size],
            mx: vec![0; size],
            add: vec![0; size],
        }
    }

    fn apply(&mut self, node: usize, delta: i32) {
        self.mn[node] += delta;
        self.mx[node] += delta;
        self.add[node] += delta;
    }

    fn push(&mut self, node: usize) {
        let d = self.add[node];
        if d != 0 {
            self.apply(node * 2, d);
            self.apply(node * 2 + 1, d);
            self.add[node] = 0;
        }
    }

    fn range_add(
        &mut self,
        node: usize,
        l: usize,
        r: usize,
        ql: usize,
        qr: usize,
        delta: i32,
    ) {
        if qr < l || r < ql {
            return;
        }
        if ql <= l && r <= qr {
            self.apply(node, delta);
            return;
        }
        self.push(node);
        let mid = (l + r) / 2;
        self.range_add(node * 2, l, mid, ql, qr, delta);
        self.range_add(node * 2 + 1, mid + 1, r, ql, qr, delta);
        self.mn[node] = self.mn[node * 2].min(self.mn[node * 2 + 1]);
        self.mx[node] = self.mx[node * 2].max(self.mx[node * 2 + 1]);
    }

    // Leftmost index in [ql, qr] whose value is 0, if any.
    // A node whose whole [min, max] range misses zero cannot
    // hold one, so it is pruned; leaves are checked exactly.
    fn first_zero(
        &mut self,
        node: usize,
        l: usize,
        r: usize,
        ql: usize,
        qr: usize,
    ) -> Option<usize> {
        if qr < l || r < ql || self.mn[node] > 0 || self.mx[node] < 0 {
            return None;
        }
        if l == r {
            return Some(l);
        }
        self.push(node);
        let mid = (l + r) / 2;
        if let Some(x) = self.first_zero(node * 2, l, mid, ql, qr) {
            return Some(x);
        }
        self.first_zero(node * 2 + 1, mid + 1, r, ql, qr)
    }
}

impl Solution {
    pub fn longest_balanced(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        if n == 0 {
            return 0;
        }
        let mut tree = SegTree::new(n);
        let mut last: HashMap<i32, usize> = HashMap::new();
        let mut ans = 0i32;
        for (r, &x) in nums.iter().enumerate() {
            let s = if x % 2 != 0 { 1 } else { -1 };
            let p = last.get(&x).copied().unwrap_or(usize::MAX);
            last.insert(x, r);
            // The newly distinct value counts for starts after
            // its previous occurrence, or from 0 if it is new.
            let lo = if p == usize::MAX { 0 } else { p + 1 };
            tree.range_add(1, 0, n - 1, lo, r, s);
            if let Some(l) = tree.first_zero(1, 0, n - 1, 0, r) {
                ans = ans.max((r - l + 1) as i32);
            }
        }
        ans
    }
}
