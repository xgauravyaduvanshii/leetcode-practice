use std::collections::VecDeque;

impl Solution {
    pub fn is_transformable(s: String, t: String) -> bool {
        // My thinking: sorting can only move a digit left past
        // bigger digits, never past a smaller one — so each
        // digit in t must come before any smaller digit still
        // waiting in s.
        let mut pos: Vec<VecDeque<usize>> = vec![VecDeque::new(); 10];
        for (i, b) in s.bytes().enumerate() {
            pos[(b - b'0') as usize].push_back(i);
        }
        for b in t.bytes() {
            let d = (b - b'0') as usize;
            if pos[d].is_empty() {
                return false;
            }
            let p = pos[d].pop_front().unwrap();
            for smaller in 0..d {
                if let Some(&q) = pos[smaller].front() {
                    if q < p {
                        return false;
                    }
                }
            }
        }
        true
    }
}
