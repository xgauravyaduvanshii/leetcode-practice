// LeetCode 2569. Handling Sum Queries After Update — Hard
// https://leetcode.com/problems/handling-sum-queries-after-update/
// Submission 2201823790 — Accepted, Rust
//
// My thinking: the second array only
// ever grows by the number of ones times
// p, so I keep its running total beside
// me and spend my effort on the first
// array — a lazy segment tree that flips
// whole ranges and always knows how many
// ones are standing.

impl Solution {
    pub fn handle_query(nums1: Vec<i32>, nums2: Vec<i32>, queries: Vec<Vec<i32>>) -> Vec<i64> {
        let n = nums1.len();
        let mut size = 1usize;
        while size < n {
            size *= 2;
        }
        let mut tree = vec![0i64; 2 * size];
        let mut lazy = vec![false; 2 * size];
        for (i, &v) in nums1.iter().enumerate() {
            tree[size + i] = v as i64;
        }
        for i in (1..size).rev() {
            tree[i] = tree[2 * i] + tree[2 * i + 1];
        }
        fn apply(tree: &mut Vec<i64>, lazy: &mut Vec<bool>, node: usize, length: i64) {
            tree[node] = length - tree[node];
            lazy[node] = !lazy[node];
        }
        fn push(tree: &mut Vec<i64>, lazy: &mut Vec<bool>, node: usize, length: i64) {
            if lazy[node] && length > 1 {
                let half = length / 2;
                apply(tree, lazy, 2 * node, half);
                apply(tree, lazy, 2 * node + 1, half);
                lazy[node] = false;
            }
        }
        fn flip(
            tree: &mut Vec<i64>,
            lazy: &mut Vec<bool>,
            node: usize,
            nl: i64,
            nr: i64,
            l: i64,
            r: i64,
        ) {
            if r < nl || nr < l {
                return;
            }
            if l <= nl && nr <= r {
                apply(tree, lazy, node, nr - nl + 1);
                return;
            }
            push(tree, lazy, node, nr - nl + 1);
            let mid = (nl + nr) / 2;
            flip(tree, lazy, 2 * node, nl, mid, l, r);
            flip(tree, lazy, 2 * node + 1, mid + 1, nr, l, r);
            tree[node] = tree[2 * node] + tree[2 * node + 1];
        }
        let mut total2: i64 = nums2.iter().map(|&x| x as i64).sum();
        let mut ans: Vec<i64> = Vec::new();
        for q in &queries {
            if q[0] == 1 {
                flip(&mut tree, &mut lazy, 1, 0, size as i64 - 1, q[1] as i64, q[2] as i64);
            } else if q[0] == 2 {
                total2 += tree[1] * q[1] as i64;
            } else {
                ans.push(total2);
            }
        }
        ans
    }
}
