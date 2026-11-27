// LeetCode 2209. Minimum White Tiles After Covering With Carpets — Hard
// https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/
// Submission 2201620619 — Accepted, Rust
//
// My thinking: I walk the floor tile by tile
// — each tile either stays visible or gets
// covered by a carpet ending here, and the
// cheapest choice at every tile with every
// carpet count is the answer.

impl Solution {
    pub fn minimum_white_tiles(floor: String, num_carpets: i32, carpet_len: i32) -> i32 {
        let chars: Vec<char> = floor.chars().collect();
        let n = chars.len();
        let k = num_carpets as usize;
        let cl = carpet_len as usize;
        let inf = i32::MAX / 2;
        let mut dp = vec![vec![inf; k + 1]; n + 1];
        for j in 0..=k {
            dp[0][j] = 0;
        }
        for i in 1..=n {
            let white = if chars[i - 1] == '1' { 1 } else { 0 };
            for j in 0..=k {
                dp[i][j] = dp[i - 1][j] + white;
                if j > 0 {
                    let prev = if i >= cl { i - cl } else { 0 };
                    dp[i][j] = dp[i][j].min(dp[prev][j - 1]);
                }
            }
        }
        dp[n][k]
    }
}
