impl Solution {
    pub fn cherry_pickup(grid: Vec<Vec<i32>>) -> i32 {
        // My thinking: the two robots walk down together, so
        // track both columns at once — each step tries all
        // nine moves and takes the cherries once if they meet.
        let rows = grid.len();
        let cols = grid[0].len();
        const NEG: i32 = i32::MIN / 2;
        let mut dp = vec![vec![NEG; cols]; cols];
        dp[0][cols - 1] = grid[0][0] + grid[0][cols - 1];
        for r in 1..rows {
            let mut new = vec![vec![NEG; cols]; cols];
            for c1 in 0..cols {
                for c2 in 0..cols {
                    if dp[c1][c2] == NEG {
                        continue;
                    }
                    for d1 in -1..=1 {
                        for d2 in -1..=1 {
                            let nc1 = c1 as i32 + d1;
                            let nc2 = c2 as i32 + d2;
                            if nc1 >= 0 && nc1 < cols as i32 && nc2 >= 0 && nc2 < cols as i32 {
                                let nc1 = nc1 as usize;
                                let nc2 = nc2 as usize;
                                let mut gain = grid[r][nc1];
                                if nc2 != nc1 {
                                    gain += grid[r][nc2];
                                }
                                new[nc1][nc2] = new[nc1][nc2].max(dp[c1][c2] + gain);
                            }
                        }
                    }
                }
            }
            dp = new;
        }
        dp.iter().flat_map(|row| row.iter()).max().copied().unwrap()
    }
}
