// LeetCode 3256. Maximum Value Sum by Placing Three Rooks I — Hard
// https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/
// Submission 2202149736 — Accepted, Rust
//
// My thinking: a rook's best cells are always
// among its row's top 3, since only two other
// rooks can block its columns. I keep each
// row's top 3, sort rows by their best cell,
// and try every triple of rows with distinct
// columns, keeping the largest sum.

impl Solution {
    pub fn maximum_value_sum(board: Vec<Vec<i32>>) -> i64 {
        let mut rows: Vec<Vec<(i64, usize)>> = Vec::new();
        for row in &board {
            let mut idx: Vec<usize> = (0..row.len()).collect();
            idx.sort_by_key(|&j| std::cmp::Reverse(row[j]));
            idx.truncate(3);
            rows.push(idx.into_iter().map(|j| (row[j] as i64, j)).collect());
        }
        rows.sort_by_key(|r| std::cmp::Reverse(r[0].0));
        let m = rows.len();
        let mut best: i64 = i64::MIN / 4;
        for i in 0..m - 2 {
            for j in i + 1..m - 1 {
                for k in j + 1..m {
                    for &(v1, c1) in &rows[i] {
                        for &(v2, c2) in &rows[j] {
                            if c1 == c2 {
                                continue;
                            }
                            for &(v3, c3) in &rows[k] {
                                if c3 == c1 || c3 == c2 {
                                    continue;
                                }
                                best = best.max(v1 + v2 + v3);
                            }
                        }
                    }
                }
            }
        }
        best
    }
}
