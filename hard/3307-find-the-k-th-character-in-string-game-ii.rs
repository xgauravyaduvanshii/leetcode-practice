// 3307. Find the K-th Character in String Game II (Hard)
// https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/
// Submission 2202316338 -- Accepted, Rust
impl Solution {
    pub fn kth_character(k: i64, operations: Vec<i32>) -> String {
        // My thinking: the word doubles at every operation, so I only need the
        // lengths up to k (capped, since anything past k behaves the same). I
        // find the first operation where the word reaches k characters, then
        // walk backwards: whenever k falls in the appended half, I subtract
        // the length before that operation, and if the operation was type 1
        // (append the shifted copy) the character I am looking for was shifted
        // once more. Starting from 'a' plus the total shift gives the answer.
        let mut lengths: Vec<i64> = vec![1];
        for _ in operations.iter() {
            let nxt = (lengths[lengths.len() - 1] * 2).min(k + 1);
            lengths.push(nxt);
            if nxt > k {
                break;
            }
        }
        let mut j = 0;
        while lengths[j] < k {
            j += 1;
        }
        let mut shift: i64 = 0;
        let mut pos = k;
        for i in (0..j).rev() {
            if pos > lengths[i] {
                pos -= lengths[i];
                if operations[i] == 1 {
                    shift += 1;
                }
            }
        }
        (((b'a' + (shift % 26) as u8) as char)).to_string()
    }
}
