// LeetCode 2454. Next Greater Element IV — Hard
// https://leetcode.com/problems/next-greater-element-iv/
// Submission 2201752366 — Accepted, Rust
//
// My thinking: the second greater is the
// first thing past the first greater that
// still beats me — I find the first
// greater with a plain monotonic stack,
// then ask a segment tree for the first
// spot after it whose value tops mine.
// (A two-stack shortcut looks tempting
// but it buries small waiters under a
// bigger one and skips their answer.)

impl Solution {
    pub fn second_greater_element(nums: Vec<i32>) -> Vec<i32> {
        let n = nums.len();
        let mut nge = vec![-1i64; n];
        let mut stack: Vec<usize> = Vec::new();
        for i in (0..n).rev() {
            while let Some(&top) = stack.last() {
                if nums[top] <= nums[i] {
                    stack.pop();
                } else {
                    break;
                }
            }
            if let Some(&top) = stack.last() {
                nge[i] = top as i64;
            }
            stack.push(i);
        }
        let mut size = 1usize;
        while size < n {
            size *= 2;
        }
        let mut tree = vec![0i32; 2 * size];
        for (i, &x) in nums.iter().enumerate() {
            tree[size + i] = x;
        }
        for i in (1..size).rev() {
            tree[i] = tree[2 * i].max(tree[2 * i + 1]);
        }
        fn find_first(tree: &[i32], node: usize, nl: usize, nr: usize, lo: usize, hi: usize, threshold: i32) -> i64 {
            if nr < lo || nl > hi || tree[node] <= threshold {
                return -1;
            }
            if nl == nr {
                return nl as i64;
            }
            let mid = (nl + nr) / 2;
            let left = find_first(tree, 2 * node, nl, mid, lo, hi, threshold);
            if left != -1 {
                return left;
            }
            find_first(tree, 2 * node + 1, mid + 1, nr, lo, hi, threshold)
        }
        let mut ans = vec![-1i32; n];
        for i in 0..n {
            let j = nge[i];
            if j == -1 {
                continue;
            }
            let k = find_first(&tree, 1, 0, size - 1, (j + 1) as usize, n - 1, nums[i]);
            if k != -1 {
                ans[i] = nums[k as usize];
            }
        }
        ans
    }
}
