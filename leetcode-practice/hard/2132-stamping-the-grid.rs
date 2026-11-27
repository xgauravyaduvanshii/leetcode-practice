// LeetCode 2132. Stamping the Grid — Hard
// https://leetcode.com/problems/stamping-the-grid/
// Submission 2201584849 — Accepted, Rust
//
// My thinking: a stamp only lands where its
// whole footprint is empty, so I add up the
// grid to test every landing, then paint all
// the landings at once and see whether every
// empty cell got covered. When the stamp is
// bigger than the grid no landing exists at
// all, so the answer is just whether the grid
// has no empty cell left.

impl Solution {
    pub fn possible_to_stamp(grid: Vec<Vec<i32>>, stamp_height: i32, stamp_width: i32) -> bool {
        let m = grid.len();
        let n = grid[0].len();
        let sh = stamp_height as usize;
        let sw = stamp_width as usize;
        if sh > m || sw > n {
            return grid.iter().all(|row| row.iter().all(|&c| c == 1));
        }
        // prefix[i+1][j+1]: occupied cells in the top-left i x j corner.
        let mut prefix = vec![vec![0; n + 1]; m + 1];
        for i in 0..m {
            let mut row_sum = 0;
            for j in 0..n {
                row_sum += grid[i][j];
                prefix[i + 1][j + 1] = prefix[i][j + 1] + row_sum;
            }
        }
        let region_sum = |r1: usize, c1: usize, r2: usize, c2: usize| {
            prefix[r2][c2] - prefix[r1][c2] - prefix[r2][c1] + prefix[r1][c1]
        };
        let mut diff = vec![vec![0; n + 1]; m + 1];
        for i in 0..=(m - sh) {
            for j in 0..=(n - sw) {
                if region_sum(i, j, i + sh, j + sw) == 0 {
                    diff[i][j] += 1;
                    diff[i + sh][j] -= 1;
                    diff[i][j + sw] -= 1;
                    diff[i + sh][j + sw] += 1;
                }
            }
        }
        // cover[i+1][j+1]: how many landings cover cell (i, j).
        let mut cover = vec![vec![0; n + 1]; m + 1];
        for i in 0..m {
            for j in 0..n {
                cover[i + 1][j + 1] =
                    diff[i][j] + cover[i][j + 1] + cover[i + 1][j] - cover[i][j];
                if grid[i][j] == 0 && cover[i + 1][j + 1] == 0 {
                    return false;
                }
            }
        }
        true
    }
}
