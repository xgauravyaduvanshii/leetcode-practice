// LeetCode 1958. Check if Move is Legal — Medium
// https://leetcode.com/problems/check-if-move-is-legal/
// Submission 2204258647 — Accepted, Rust

// My thinking: a move is legal when, in at least one of the eight
// directions, the new piece sits next to a run of one or more
// opponent pieces that is then closed off by one of my own pieces.
// So I walk each direction from the move, counting opponent pieces,
// and the move is legal the moment a walk with at least one opponent
// piece lands on my own colour. An empty cell or the board edge ends
// that direction with no legal line.
impl Solution {
    pub fn check_move(board: Vec<Vec<char>>, r_move: i32, c_move: i32, color: char) -> bool {
        let opponent = if color == 'B' { 'W' } else { 'B' };
        for (dr, dc) in [
            (-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1),
        ] {
            let (mut r, mut c) = (r_move + dr, c_move + dc);
            let mut seen_opponent = 0;
            while (0..8).contains(&r)
                && (0..8).contains(&c)
                && board[r as usize][c as usize] == opponent
            {
                seen_opponent += 1;
                r += dr;
                c += dc;
            }
            if seen_opponent > 0
                && (0..8).contains(&r)
                && (0..8).contains(&c)
                && board[r as usize][c as usize] == color
            {
                return true;
            }
        }
        false
    }
}
