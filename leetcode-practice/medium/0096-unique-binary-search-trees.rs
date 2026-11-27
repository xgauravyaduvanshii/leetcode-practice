// LeetCode 96. Unique Binary Search Trees — Medium
// https://leetcode.com/problems/unique-binary-search-trees/
// Submission 2203982662 — Accepted, Rust

// My thinking:
// We need the number of structurally unique BSTs that can be built from
// the values 1..n. The key idea is that the values are already sorted,
// so any BST is fully decided by which value sits at the root: everything
// smaller must go in the left subtree, everything larger in the right.
//
// Pick value i as the root. Then the left subtree uses the i-1 smaller
// values and the right subtree uses the n-i larger values. The two sides
// are independent, so for this root there are
//     (ways for i-1 nodes) * (ways for n-i nodes)
// different trees. Add that up over every possible root i = 1..n.
//
// That gives a recurrence: dp[0] = 1 (one way to arrange nothing — the
// empty tree), dp[n] = sum over i of dp[i-1] * dp[n-i]. Build dp bottom-up
// from 0 to n. This is the Catalan number sequence: 1, 1, 2, 5, 14, 42...
// Time O(n^2), space O(n).

impl Solution {
    pub fn num_trees(n: i32) -> i32 {
        // dp[k] = number of unique BSTs with k nodes
        let n = n as usize;
        let mut dp: Vec<i64> = vec![0; n + 1];
        dp[0] = 1; // empty tree: exactly one way

        for nodes in 1..=n {
            let mut total: i64 = 0;
            // try each value 1..=nodes as the root
            for root in 1..=nodes {
                let left_size = root - 1;
                let right_size = nodes - root;
                total += dp[left_size] * dp[right_size];
            }
            dp[nodes] = total;
        }

        dp[n] as i32
    }
}
