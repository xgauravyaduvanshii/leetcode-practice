// LeetCode 2326. Spiral Matrix IV — Medium
// https://leetcode.com/problems/spiral-matrix-iv/
// Submission 2204691470 — Accepted, Rust
//
// My thinking: same idea as the Python version — fill a -1 matrix by
// walking a spiral (right, down, left, up), writing each linked-list
// value into the current cell and turning clockwise whenever the next
// cell is out of bounds or already filled.
// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Clone, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
//
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn spiral_matrix(m: i32, n: i32, head: Option<Box<ListNode>>) -> Vec<Vec<i32>> {
        let m = m as usize;
        let n = n as usize;
        let mut mat = vec![vec![-1; n]; m];
        let dirs: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];
        let mut d = 0usize;
        let (mut i, mut j) = (0i32, 0i32);
        let mut node = head;
        while let Some(cur) = node {
            mat[i as usize][j as usize] = cur.val;
            node = cur.next;
            let (mut ni, mut nj) = (i + dirs[d].0, j + dirs[d].1);
            if ni < 0 || ni >= m as i32 || nj < 0 || nj >= n as i32 || mat[ni as usize][nj as usize] != -1 {
                d = (d + 1) % 4;
                ni = i + dirs[d].0;
                nj = j + dirs[d].1;
            }
            i = ni;
            j = nj;
        }
        mat
    }
}
