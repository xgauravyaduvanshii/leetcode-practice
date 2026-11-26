// LeetCode 3999. Minimum Number of String Groups Through Transformations — Hard
// https://leetcode.com/problems/minimum-number-of-string-groups-through-transformations/
// Submission 2203503393 — Accepted, Rust
//
// My thinking: a transformation rotates the
// even-index subsequence and the odd-index
// subsequence independently, so two words are
// equivalent exactly when their even parts are
// rotations of each other and their odd parts are
// rotations of each other. Rotation is an
// equivalence relation, so each group is one
// equivalence class: canonicalise every word by
// its least lexicographic rotation of each part
// (Booth's algorithm, linear time) and count the
// distinct keys. Words of different lengths can
// never collide, since the rotated parts keep
// their lengths.
use std::collections::HashSet;

fn least_rotation(s: &[u8]) -> Vec<u8> {
    let n = s.len();
    if n == 0 {
        return Vec::new();
    }
    let mut ss = Vec::with_capacity(2 * n);
    ss.extend_from_slice(s);
    ss.extend_from_slice(s);
    let (mut i, mut j, mut k) = (0usize, 1usize, 0usize);
    while i < n && j < n && k < n {
        let a = ss[i + k];
        let b = ss[j + k];
        if a == b {
            k += 1;
        } else if a < b {
            j += k + 1;
            k = 0;
        } else {
            i += k + 1;
            k = 0;
        }
        if i == j {
            i += 1;
        }
    }
    let start = std::cmp::min(i, j);
    ss[start..start + n].to_vec()
}

impl Solution {
    pub fn minimum_groups(words: Vec<String>) -> i32 {
        let mut keys: HashSet<(Vec<u8>, Vec<u8>)> = HashSet::new();
        for w in words {
            let bytes = w.as_bytes();
            let even: Vec<u8> = bytes.iter().step_by(2).cloned().collect();
            let odd: Vec<u8> = bytes.iter().skip(1).step_by(2).cloned().collect();
            keys.insert((least_rotation(&even), least_rotation(&odd)));
        }
        keys.len() as i32
    }
}
