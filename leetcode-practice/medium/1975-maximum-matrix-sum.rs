// LeetCode 1975. Maximum Matrix Sum — Medium
// https://leetcode.com/problems/maximum-matrix-sum/
// Submission 2204085356 — Accepted, Rust

// My thinking: flipping two adjacent cells changes the negative count
// by -2, 0, or +2, so its parity never changes. With an even number of
// negatives I can make every entry positive and the answer is the sum
// of all absolute values. With an odd number one entry must stay
// negative, so I leave the one with the smallest absolute value
// negative, losing twice that value. A zero makes the loss zero.
impl Solution {
    pub fn max_matrix_sum(matrix: Vec<Vec<i32>>) -> i64 {
        let mut total: i64 = 0;
        let mut negatives = 0;
        let mut min_abs: i64 = i64::MAX;

        for row in &matrix {
            for &value in row {
                let a = (value as i64).abs();
                total += a;
                if value < 0 {
                    negatives += 1;
                }
                min_abs = min_abs.min(a);
            }
        }

        if negatives % 2 == 1 {
            total -= 2 * min_abs;
        }

        total
    }
}
