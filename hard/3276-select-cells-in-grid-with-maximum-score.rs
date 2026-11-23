// LeetCode 3276. Select Cells in Grid With Maximum Score — Hard
// https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/
// Submission 2202174053 — Accepted, Rust
//
// My thinking: each value can be taken at most
// once, from a row that contains it, and each
// row at most once. I process values largest
// first and keep a bitmask DP over which rows
// are already used: for each value I either skip
// it or take it from one of its unused rows. The
// answer is the best score over all masks.

impl Solution {
    pub fn max_score(grid: Vec<Vec<i32>>) -> i32 {
        let m = grid.len();
        let mut rows_for_value = [0usize; 101];
        for (r, row) in grid.iter().enumerate() {
            for &v in row.iter() {
                rows_for_value[v as usize] |= 1usize << r;
            }
        }
        let size = 1usize << m;
        let mut dp = vec![-1000000000i32; size];
        dp[0] = 0;
        for v in (1..=100).rev() {
            let rows = rows_for_value[v as usize];
            if rows == 0 {
                continue;
            }
            let mut ndp = dp.clone();
            for mask in 0..size {
                let cur = dp[mask];
                if cur < 0 {
                    continue;
                }
                let mut avail = rows & !mask;
                while avail != 0 {
                    let lsb = avail & avail.wrapping_neg();
                    let nmask = mask | lsb;
                    if ndp[nmask] < cur + v {
                        ndp[nmask] = cur + v;
                    }
                    avail ^= lsb;
                }
            }
            dp = ndp;
        }
        *dp.iter().max().unwrap()
    }
}
