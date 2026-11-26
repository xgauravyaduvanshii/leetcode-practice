// LeetCode 2017. Grid Game — Medium
// https://leetcode.com/problems/grid-game/
// Submission 2204143983 — Accepted, Rust

// My thinking: the first robot must walk from the top-left corner to the
// bottom-right corner, moving only right or down, so it goes right along
// the top row for a while, drops down at some column i, then goes right
// along the bottom row. Every cell it steps on is emptied, so the second
// robot, taking the same kind of path, can only score from the cells the
// first robot did not touch: the top-row cells after column i, or the
// bottom-row cells before column i. It takes the better of those two, so
// for a given drop column i its score is max(top suffix after i, bottom
// prefix before i). The first robot picks the drop column that makes that
// best score as small as possible, so I try every column and keep the
// smallest of those maxima.
impl Solution {
    pub fn grid_game(grid: Vec<Vec<i32>>) -> i32 {
        let n = grid[0].len();
        // Points left in the top row after the drop column: starts as the
        // whole top row except column 0 and shrinks as i moves right.
        let mut top_suffix: i64 = grid[0][1..].iter().map(|&x| x as i64).sum();
        // Points left in the bottom row before the drop column: starts at
        // 0 and grows as i moves right.
        let mut bottom_prefix: i64 = 0;
        let mut ans = i64::MAX;
        for i in 0..n {
            ans = ans.min(top_suffix.max(bottom_prefix));
            // Moving the drop one column right: column i + 1 leaves the
            // top suffix, and column i joins the bottom prefix.
            if i + 1 < n {
                top_suffix -= grid[0][i + 1] as i64;
            }
            bottom_prefix += grid[1][i] as i64;
        }
        ans as i32
    }
}
